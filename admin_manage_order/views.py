from django.shortcuts import render,HttpResponseRedirect,HttpResponse,get_object_or_404
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from orders.models import AwOrders,AwOrederItem,AwOrderNote
# from .forms import AwProductsForm
from admin_manage_Vintages.models import AwVintages
from datetime import datetime
from profile_user.models import AwUserInfo
from django.contrib import messages
from django.urls import reverse
from datetime import datetime
from datetime import date
from django.template.defaulttags import register
from django.urls import reverse_lazy
from django.core.files.base import ContentFile
import base64
from django.template.loader import render_to_string
from django.db.models import Q
from addressbook_user.forms import AwAddressBookForm

# .---------------------------------
from django.conf import settings
from addressbook_user.models import AwAddressBook
from addressbook_user.forms import AwAddressBookForm
from orders.forms import AwOrderNoteForm

# ----------------------------------

# Create your views here.






@register.filter(name='get_user_number')
def get_user_number(user_ins):
    contact_no = ''
    if AwUserInfo.objects.filter(User=user_ins).exists():
        get_user_info = get_object_or_404(AwUserInfo,User=user_ins)
        contact_no = get_user_info.Contact_no
    return contact_no

@method_decorator(login_required , name="dispatch")
class ManageOrdersDeliveryView(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/orders/delivery_order_list.html'

    def get(self, request, *args, **kwargs):
        queryset = None
        if AwOrders.objects.filter(~Q(Order_Type='Caller')).exists():
            queryset = AwOrders.objects.filter(~Q(Order_Type='Caller')).order_by("-id")
        return render(request, self.template_name, { 'Page_title': "Manage Delivery Orders", 'queryset': queryset})


@method_decorator(login_required , name="dispatch")
class ManageOrdersCallerView(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/orders/caller_order_list.html'

    def get(self, request, *args, **kwargs):
        queryset = None
        if AwOrders.objects.filter(Order_Type='Caller').exists():
            queryset = AwOrders.objects.filter(Order_Type='Caller').order_by("-id")
        return render(request, self.template_name, { 'Page_title': "Manage Caller Orders", 'queryset': queryset})



@method_decorator(login_required , name="dispatch")
class ManageOrdersAccordingToTypeView(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/orders/index.html'

    def get(self, request, *args, **kwargs):
        type = self.kwargs.get("type").lower()
        if type == 'failled':
            type = 'Failled'
        if type == 'refunded':
            type = 'Refunded'
        if type == 'cancelled':
            type = 'Cancelled'
        if type == 'active':
            type = 'Active'
        if type == 'complete':
            type = 'Complete'
        queryset = None
        if AwOrders.objects.filter(Order_Status_Set=type).exists():
            queryset = AwOrders.objects.filter(Order_Status_Set=type).order_by("-id")
        return render(request, self.template_name, { 'Page_title': "Manage Orders "+type, 'queryset': queryset})


@method_decorator(login_required , name="dispatch")
class ManageOrdersView(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/orders/index.html'

    def get(self, request, *args, **kwargs):
        queryset = AwOrders.objects.all().order_by("-id")
        return render(request, self.template_name, { 'Page_title': "Manage Orders", 'queryset': queryset})





def order_status_update(request,order_id,status):
    if AwOrders.objects.filter(order_id=order_id).exists():
        AwOrders.objects.filter(order_id=order_id).update(Order_Status_Set=status)
        messages.info(request, "Order update successfully !")
    else:
        messages.error(request, "order_id is incorreect!")
    return HttpResponseRedirect(reverse('admin_manage_order:edit_order', args=(order_id,)))


def delete_note(request,id,order_id):
    if AwOrderNote.objects.filter(id=id).exists():
        AwOrderNote.objects.get(id=id).delete()
        messages.info(request, "Note removed !")
    else:
        messages.error(request, "Note id is incorreect!")
    return HttpResponseRedirect(reverse('admin_manage_order:edit_order', args=(order_id,)))


@method_decorator(login_required , name="dispatch")
class EditOrdersView(SuccessMessageMixin,generic.TemplateView):
    template_name = 'admin/orders/edit-order.html'


    def get_context_data(self, *args, **kwargs):
        context = super(EditOrdersView, self).get_context_data(*args, **kwargs)
        context['Page_title'] = "Edit Order"
        order_id = self.kwargs.get("order_id")
        get_order_ins = get_object_or_404(AwOrders, order_id=order_id)
        context['order_ins'] = get_order_ins
        order_items = None
        if AwOrederItem.objects.filter(Order_id__order_id = order_id).exists():
            order_items = AwOrederItem.objects.filter(Order_id__order_id = order_id)
        context['order_items'] = order_items
        address_form = AwAddressBookForm(instance=get_order_ins.Order_address)
        context['address_form'] = address_form
        context['note_form'] = AwOrderNoteForm

        order_notes = None
        if AwOrderNote.objects.filter(Order_id__order_id = order_id).exists():
            order_notes = AwOrderNote.objects.filter(Order_id__order_id = order_id).order_by('-id')
        context['order_notes'] = order_notes
        context['BASE_URL'] = settings.BASE_URL
        order_status_list = ['Complete','Cancelled','Refunded','Failled','Pending']
        context['order_status_list'] = order_status_list
        return context

    def post(self, request, *args, **kwargs):
        if request.POST['form_type'] == "address_update":
            id = request.POST['id'];
            order_id = request.POST['order_id'];
            address_ins = AwAddressBook.objects.get(id=id)
            address_form = AwAddressBookForm(data=(request.POST or None), instance=address_ins)
            if address_form.is_valid():
                try:
                    data = address_form.save(commit=False)
                    data.Update_Date = datetime.now()
                    data.save()
                    messages.info(request, "Address update successfully !")
                except Exception as e:
                    messages.error(request, str(e))
            else:
                messages.error(request, address_form.errors)
            return HttpResponseRedirect(reverse('admin_manage_order:edit_order', args=(order_id,)))
        if request.POST['form_type'] == "order_note":
            order_id = request.POST['order_id'];
            get_order_ins = get_object_or_404(AwOrders, order_id=order_id)
            get_not_form = AwOrderNoteForm(request.POST, request.FILES)
            if get_not_form.is_valid():
                # try:
                data = get_not_form.save(commit=False)
                data.User = request.user
                data.Order_id =get_order_ins
                data.save()
                messages.info(request, "Note Add successfully !")
                # except Exception as e:
                #     messages.error(request, str(e))
            else:
                messages.error(request, get_not_form.errors)
            return HttpResponseRedirect(reverse('admin_manage_order:edit_order', args=(order_id,)))
        return HttpResponseRedirect(reverse('admin_manage_order:orders'))

