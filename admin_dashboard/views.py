from django.shortcuts import render,HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from admin_manage_products.models import AwProducts
from django.db.models import Count
from django.contrib.auth.models import User
from orders.models import AwOrders,AwOrederItem
# Create your views here.

@method_decorator(login_required , name="dispatch")
class AdminDashboardVIew(generic.TemplateView):
    template_name = 'admin/dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Dashoard"
        total_User = User.objects.all().count()
        total_Caller_Orders = 0
        if AwOrders.objects.filter(Order_Type='Caller'):
            total_Caller_Orders = AwOrders.objects.filter(Order_Type='Caller').count()
        total_delivery_Orders = 0
        if AwOrders.objects.filter(Order_Type='Delivered'):
            total_delivery_Orders = AwOrders.objects.filter(Order_Type='Delivered').count()
        total_complate_product = 0
        if AwOrders.objects.filter(Order_Status_Set='Complete'):
            total_complate_product = AwOrders.objects.filter(Order_Status_Set='Complete').count()
        context['total_User'] = total_User
        context['total_complate_product'] = total_complate_product
        context['total_delivery_Orders'] = total_delivery_Orders
        context['total_Caller_Orders'] = total_Caller_Orders
        return context