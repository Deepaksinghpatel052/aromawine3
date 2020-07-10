from django.shortcuts import render,HttpResponseRedirect,HttpResponse,get_object_or_404
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from orders.models import AwOrders
# from .forms import AwProductsForm
from admin_manage_Vintages.models import AwVintages
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

# .---------------------------------
from addressbook_user.models import AwAddressBook
from addressbook_user.forms import AwAddressBookForm

# ----------------------------------

# Create your views here.
# Create your views here.





@method_decorator(login_required , name="dispatch")
class ManageOrdersView(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/orders/index.html'


    def get(self, request, *args, **kwargs):
        queryset = AwOrders.objects.all().order_by("-id")
        # context  = super(ManageOrdersView,self).get_context_data(*args,**kwargs)
        # context['Page_title'] = "Manage Orders"
        # print(context)
        # return context

        return render(request, self.template_name, { 'Page_title': "Manage Orders", 'queryset': queryset})

@method_decorator(login_required , name="dispatch")
class EditOrder(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/orders/edit-order.html'
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("id")
        queryset = AwOrders.objects.get(pk=id)
        # get_instance = get_object_or_404(AwAddressBook, id=pk,User = request.user)
        get_instance = queryset.User
        address_data=""
        if AwAddressBook.objects.filter(User=get_instance).exists():
            address_data = AwAddressBook.objects.get(User=get_instance)
        return render(request, self.template_name, { 'Page_title': "Edit Orders", 'queryset': queryset,'address_data':address_data})




@method_decorator(login_required , name="dispatch")
class CancelOrder(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/orders/edit-order.html'

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("id")
        AwOrders.objects.filter(pk=id).update(Order_Status="Cancelled")
        queryset = AwOrders.objects.get(pk=id)
        return HttpResponseRedirect(reverse('admin_manage_order:orders'))
        # return render(request, self.template_name, { 'Page_title': "Edit Orders", 'queryset': queryset})

@method_decorator(login_required , name="dispatch")
class ChangeOrderStatus(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/orders/edit-order.html'

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("id")
        status = request.GET.get('check', '')

        AwOrders.objects.filter(pk=id).update(Order_Status=status)
        queryset = AwOrders.objects.get(pk=id)
        # context  = super(ManageOrdersView,self).get_context_data(*args,**kwargs)
        # context['Page_title'] = "Manage Orders"
        # print(context)
        # return context

        return render(request, self.template_name, { 'Page_title': "Edit Orders", 'queryset': queryset})


@method_decorator(login_required , name="dispatch")
class CellerOrder(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/orders/celler-order.html'
    queryset = AwOrders.objects.all().order_by("-id")

    def get_context_data(self, *args,**kwargs):
        context  = super(CellerOrder,self).get_context_data(*args,**kwargs)
        context['Page_title'] = "Celler Orders"
        print(context)
        return context


@method_decorator(login_required , name="dispatch")
class RefundedOrder(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/orders/refunded-order.html'

    def get(self, request, *args, **kwargs):
        queryset = AwOrders.objects.filter(Order_Status="Refunded").order_by("-id")
        return render(request, self.template_name, { 'Page_title': "Refunded Orders", 'queryset': queryset})


@method_decorator(login_required , name="dispatch")
class CanclledOrder(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/orders/canclled-order.html'

    def get(self, request, *args, **kwargs):
        queryset = AwOrders.objects.filter(Order_Status="Cancelled").order_by("-id")
        return render(request, self.template_name, { 'Page_title': "Cancelled Orders", 'queryset': queryset})


@method_decorator(login_required , name="dispatch")
class FailledOrder(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/orders/failled-order.html'

    def get(self, request, *args, **kwargs):
        queryset = AwOrders.objects.filter(Order_Status="Failled").order_by("-id")
        return render(request, self.template_name, { 'Page_title': "Failled Orders", 'queryset': queryset})




@method_decorator(login_required , name="dispatch")
class EditAddress(SuccessMessageMixin,generic.UpdateView):
    form_class = AwAddressBookForm
    template_name = 'admin/orders/edit-address.html'
    queryset = AwAddressBook.objects.all()
    success_url = reverse_lazy('admin_manage_order:orders')

    def get_success_message(self, cleaned_data):
        return "Address update successfully."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Edit-Address"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Update_Date = datetime.now()
        self.object.save()
        form.save()
        return super().form_valid(form)

