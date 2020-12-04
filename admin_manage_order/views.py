from django.shortcuts import render,HttpResponseRedirect,HttpResponse,get_object_or_404
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from orders.models import AwOrders,AwOrederItem,AwOrderNote
# from .forms import AwProductsForm
from admin_manage_Vintages.models import AwVintages
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
from django.db.models import Sum
# ----------------------------------

# Create your views here.


@register.filter(name='get_counting_of_sales_product')
def get_counting_of_sales_product(demo):
    filters = Q(Order_id__order_place=True)
    queryset = AwOrederItem.objects.filter(Quentity__gt=0).filter(Order_id__Order_Status_Set='Active').filter(filters).order_by("-id")
    return len(queryset)

@register.filter(name='get_counting_of_order')
def get_counting_of_order(order_type,order_status):
    order_type_set = order_type
    order_status_set = order_status
    count = 0
    if order_type_set == 'Tickets':
        if AwOrders.objects.filter(Order_Type=order_type_set).filter(
                order_place=True).exists():
            get_user_info = AwOrders.objects.filter(Order_Type=order_type_set).filter(order_place=True)
            count = len(get_user_info)
    elif order_type_set == 'All':
        if AwOrders.objects.filter(Order_Status_Set=order_status_set).filter(order_place=True).exists():
            get_user_info = AwOrders.objects.filter(Order_Status_Set=order_status_set).filter(order_place=True)
            count = len(get_user_info)
    else:
        if AwOrders.objects.filter(Order_Type=order_type_set).filter(Order_Status_Set=order_status_set).filter(order_place=True).exists():
            get_user_info = AwOrders.objects.filter(Order_Type=order_type_set).filter(Order_Status_Set=order_status_set).filter(order_place=True)
            count = len(get_user_info)
    return count




@register.filter(name='get_user_number')
def get_user_number(user_ins):
    contact_no = ''
    if AwUserInfo.objects.filter(User=user_ins).exists():
        get_user_info = get_object_or_404(AwUserInfo,User=user_ins)
        contact_no = get_user_info.Contact_no
    return contact_no

@method_decorator(login_required , name="dispatch")
class ManageProductSalesListView(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/orders/cellar_product.html'

    def get(self, request, *args, **kwargs):
        queryset = None
        group_by = None
        order_type = "Cellar or Delivery"
        filters = Q(Order_id__order_place=True)
        if 'product_order_type' in self.request.GET and self.request.GET['product_order_type']:
            if self.request.GET['product_order_type']=="Cellar":
                order_type  = "Cellar"
                filters = filters & Q(Order_id__Order_Type='Caller')
            elif self.request.GET['product_order_type']=="Delivery":
                filters = filters & Q(Order_id__Order_Type='Delivered')
                order_type = "Delivery"
            else:
                filters = filters & ~Q(Order_id__Order_Type='Tickets')
        start_date_1 = ""
        end_date_1 = ""
        if 'start_date' in self.request.GET and self.request.GET['start_date']:
            start_date_1 = self.request.GET['start_date']
            start_date = datetime.strptime(self.request.GET['start_date'], "%m-%d-%Y").date().strftime('%Y-%m-%d')
            if 'end_date' in self.request.GET and self.request.GET['end_date']:
                end_date = datetime.strptime(self.request.GET['end_date'], "%m-%d-%Y").date().strftime('%Y-%m-%d')
                filters = filters & Q(Order_id__Order_Date__date__range=[start_date, end_date])
                end_date_1 = self.request.GET['end_date']
                # filters = filters & Q(Order_Date__gte=self.request.GET['start_date'], Order_Date__lt=self.request.GET['start_date'])
            else:
                filters = filters & Q(Order_Date__date__range=[start_date, start_date])

        group_by_set = []
        Product_Delivered_name  = []
        Product_Cellar_name  = []
        years  = []
        if AwOrederItem.objects.filter(Quentity__gt=0).filter(Order_id__Order_Status_Set='Active').filter(filters).exists():
            queryset = AwOrederItem.objects.filter(Quentity__gt=0).filter(Order_id__Order_Status_Set='Active').filter(filters).order_by("-id")
            # group_by = AwOrederItem.objects.filter(Quentity__gt=0).filter(Order_id__Order_Status_Set='Active').filter(filters).order_by("-id")
            for item in queryset:
                status = True
                if item.Product_Delivered in Product_Delivered_name and item.Year in years and item.Order_id.Order_Type == 'Delivered':
                    status = False
                else:
                    Product_Delivered_name.append(item.Product_Delivered)
                    years.append(item.Year)
                if item.Product_Cellar in Product_Cellar_name and item.Year in years and item.Order_id.Order_Type == 'Caller':
                    status = False
                else:
                    Product_Cellar_name.append(item.Product_Delivered)
                    years.append(item.Year)
                if status:
                    group_by = {}
                    group_by['id'] = item.id
                    group_by['Order_Type'] = item.Order_id.Order_Type
                    group_by['Product_Delivered'] = item.Product_Delivered
                    group_by['Product_Cellar'] = item.Product_Cellar
                    group_by['Year'] = item.Year
                    group_by['Type'] = item.Type
                    group_by['Case_Formate_text'] = item.Case_Formate_text
                    group_by['Cost_of_product'] = item.Cost_of_product
                    group_by['Gst'] = item.Gst
                    group_by['Order_Quentity'] = item.Order_Quentity
                    group_by['Total_cost'] = item.Total_cost
                    group_by['Quentity'] = item.Quentity
                    group_by['Order_Date'] = item.Order_id.Order_Date
                    group_by_set.append(group_by)

        order_types = ["Cellar or Delivery","Cellar","Delivery"]
        return render(request, self.template_name, {'Page_title': "Product Sales List",'group_by_set':group_by_set, 'queryset': queryset,'order_type':order_type,'order_types':order_types,'start_date':start_date_1,"end_date":end_date_1})



@method_decorator(login_required , name="dispatch")
class ManageOrdersTicketView(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/orders/index.html'

    def get(self, request, *args, **kwargs):
        queryset = None
        filters = Q(order_place=True)
        start_date_1 = ""
        end_date_1 = ""
        if 'start_date' in self.request.GET and self.request.GET['start_date']:
            start_date_1 = self.request.GET['start_date']
            start_date = datetime.strptime(self.request.GET['start_date'], "%m-%d-%Y").date().strftime('%Y-%m-%d')
            if 'end_date' in self.request.GET and self.request.GET['end_date']:
                end_date_1 = self.request.GET['end_date']
                end_date = datetime.strptime(self.request.GET['end_date'], "%m-%d-%Y").date().strftime('%Y-%m-%d')
                filters = filters & Q(Order_Date__date__range=[start_date, end_date])
                # filters = filters & Q(Order_Date__gte=self.request.GET['start_date'], Order_Date__lt=self.request.GET['start_date'])
            else:
                filters = filters & Q(Order_Date__date__range=[start_date, start_date])
        if AwOrders.objects.filter(Order_Type='Tickets').filter(filters).exists():
            queryset = AwOrders.objects.filter(Order_Type='Tickets').filter(filters).order_by("-id")
        return render(request, self.template_name, { 'Page_title': "Manage Ticket Orders", 'queryset': queryset,'start_date':start_date_1,"end_date":end_date_1})



@method_decorator(login_required , name="dispatch")
class ManageOrdersDeliveryView(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/orders/delivery_order_list.html'

    def get(self, request, *args, **kwargs):
        queryset = None
        filters = Q(order_place=True)
        start_date_1 = ""
        end_date_1 = ""
        if 'start_date' in self.request.GET and self.request.GET['start_date']:
            start_date = datetime.strptime(self.request.GET['start_date'], "%m-%d-%Y").date().strftime('%Y-%m-%d')
            start_date_1 = self.request.GET['start_date']
            if 'end_date' in self.request.GET and self.request.GET['end_date']:
                end_date_1 = self.request.GET['end_date']
                end_date = datetime.strptime(self.request.GET['end_date'], "%m-%d-%Y").date().strftime('%Y-%m-%d')
                filters = filters & Q(Order_Date__date__range=[start_date, end_date])
                # filters = filters & Q(Order_Date__gte=self.request.GET['start_date'], Order_Date__lt=self.request.GET['start_date'])
            else:
                filters = filters & Q(Order_Date__date__range=[start_date, start_date])
        if AwOrders.objects.filter(~Q(Order_Type='Caller')).filter(Order_Status_Set='Active').filter(filters).exists():
            queryset = AwOrders.objects.filter(~Q(Order_Type='Caller')).filter(Order_Status_Set='Active').filter(filters).order_by("-id")
        return render(request, self.template_name, { 'Page_title': "In-Process Delivery Orders", 'queryset': queryset,'start_date':start_date_1,"end_date":end_date_1})


@method_decorator(login_required , name="dispatch")
class ManageOrdersCallerView(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/orders/caller_order_list.html'

    def get(self, request, *args, **kwargs):
        queryset = None
        filters = Q(order_place=True)
        start_date_1 = ""
        end_date_1 = ""
        if 'start_date' in self.request.GET and self.request.GET['start_date']:
            start_date_1 = self.request.GET['start_date']
            start_date = datetime.strptime(self.request.GET['start_date'], "%m-%d-%Y").date().strftime('%Y-%m-%d')
            if 'end_date' in self.request.GET and self.request.GET['end_date']:
                end_date_1 = self.request.GET['end_date']
                end_date = datetime.strptime(self.request.GET['end_date'], "%m-%d-%Y").date().strftime('%Y-%m-%d')
                filters = filters & Q(Order_Date__date__range=[start_date, end_date])
                # filters = filters & Q(Order_Date__gte=self.request.GET['start_date'], Order_Date__lt=self.request.GET['start_date'])
            else:
                filters = filters & Q(Order_Date__date__range=[start_date, start_date])
        if AwOrders.objects.filter(Order_Type='Caller').filter(Order_Status_Set='Active').filter(filters).exists():
            queryset = AwOrders.objects.filter(Order_Type='Caller').filter(Order_Status_Set='Active').filter(filters).order_by("-id")
        return render(request, self.template_name, { 'Page_title': "Manage Caller Orders", 'queryset': queryset,'start_date':start_date_1,"end_date":end_date_1})




@method_decorator(login_required , name="dispatch")
class ManageOrdersAccordingToConplateDelivery(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/orders/index.html'

    def get(self, request, *args, **kwargs):
        order_type = 'Delivered'
        type = 'Complete'
        queryset = None
        start_date_1 = ""
        end_date_1 = ""
        filters = Q(order_place=True)
        if 'start_date' in self.request.GET and self.request.GET['start_date']:
            start_date_1 = self.request.GET['start_date']
            start_date = datetime.strptime(self.request.GET['start_date'], "%m-%d-%Y").date().strftime('%Y-%m-%d')
            if 'end_date' in self.request.GET and self.request.GET['end_date']:
                end_date_1 = self.request.GET['end_date']
                end_date = datetime.strptime(self.request.GET['end_date'], "%m-%d-%Y").date().strftime('%Y-%m-%d')
                filters = filters & Q(Order_Date__date__range=[start_date, end_date])
                # filters = filters & Q(Order_Date__gte=self.request.GET['start_date'], Order_Date__lt=self.request.GET['start_date'])
            else:
                filters = filters & Q(Order_Date__date__range=[start_date, start_date])
        if AwOrders.objects.filter(Order_Status_Set=type).filter(Order_Type=order_type).filter(filters).exists():
            queryset = AwOrders.objects.filter(Order_Status_Set=type).filter(Order_Type=order_type).filter(filters).order_by("-id")
        return render(request, self.template_name, { 'Page_title': "Manage Complated "+order_type, 'queryset': queryset,'start_date':start_date_1,"end_date":end_date_1})




@method_decorator(login_required , name="dispatch")
class ManageOrdersAccordingToConplateCellar(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/orders/index.html'

    def get(self, request, *args, **kwargs):
        order_type = 'Caller'
        type = 'Complete'
        queryset = None
        filters = Q(order_place=True)
        start_date_1 = ""
        end_date_1 = ""
        if 'start_date' in self.request.GET and self.request.GET['start_date']:
            start_date_1 = self.request.GET['start_date']
            start_date = datetime.strptime(self.request.GET['start_date'], "%m-%d-%Y").date().strftime('%Y-%m-%d')
            if 'end_date' in self.request.GET and self.request.GET['end_date']:
                end_date_1 = self.request.GET['end_date']
                end_date = datetime.strptime(self.request.GET['end_date'], "%m-%d-%Y").date().strftime('%Y-%m-%d')
                filters = filters & Q(Order_Date__date__range=[start_date, end_date])
                # filters = filters & Q(Order_Date__gte=self.request.GET['start_date'], Order_Date__lt=self.request.GET['start_date'])
            else:
                filters = filters & Q(Order_Date__date__range=[start_date, start_date])
        if AwOrders.objects.filter(Order_Status_Set=type).filter(Order_Type=order_type).filter(filters).exists():
            queryset = AwOrders.objects.filter(Order_Status_Set=type).filter(Order_Type=order_type).filter(filters).order_by("-id")
        return render(request, self.template_name, { 'Page_title': "Manage Complated "+order_type+" Orders ", 'queryset': queryset,'start_date':start_date_1,"end_date":end_date_1})


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
        if type == 'complete':
            type = 'Complete'
        queryset = None
        filters = Q(order_place=True)
        start_date_1 = ""
        end_date_1 = ""
        if 'start_date' in self.request.GET and self.request.GET['start_date']:
            start_date_1 = self.request.GET['start_date']
            start_date = datetime.strptime(self.request.GET['start_date'], "%m-%d-%Y").date().strftime('%Y-%m-%d')
            if 'end_date' in self.request.GET and self.request.GET['end_date']:
                end_date_1 = self.request.GET['end_date']
                end_date = datetime.strptime(self.request.GET['end_date'], "%m-%d-%Y").date().strftime('%Y-%m-%d')
                filters = filters & Q(Order_Date__date__range=[start_date, end_date])
                # filters = filters & Q(Order_Date__gte=self.request.GET['start_date'], Order_Date__lt=self.request.GET['start_date'])
            else:
                filters = filters & Q(Order_Date__date__range=[start_date, start_date])
        if AwOrders.objects.filter(Order_Status_Set=type).filter(filters).exists():
            queryset = AwOrders.objects.filter(Order_Status_Set=type).filter(filters).order_by("-id")
        return render(request, self.template_name, { 'Page_title': "Manage Orders "+type, 'queryset': queryset,'start_date':start_date_1,"end_date":end_date_1})


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

