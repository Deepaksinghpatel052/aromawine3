from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from datetime import datetime
from datetime import date
from .models import AwCuponCode
from .forms import AwCouponForm
from django.urls import reverse_lazy
from django.core.files.base import ContentFile
import base64
# Create your views here.


@method_decorator(login_required , name="dispatch")
class ManageCouponView(SuccessMessageMixin,generic.ListView):
    queryset = AwCuponCode.objects.all().order_by("-id")
    template_name = 'admin/coupon/coupon.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ManageCouponView, self).get_context_data(*args, **kwargs)
        context['Page_title'] = "Manage Coupon"
        print(context)
        return context

@method_decorator(login_required , name="dispatch")
class CreateCouponView(SuccessMessageMixin,generic.CreateView):
    form_class = AwCouponForm
    template_name = 'admin/coupon/create.html'


    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Coupon add successfully."
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['Page_title'] = "Add Coupon"
        return context


@method_decorator(login_required , name="dispatch")
class CouponUpdateView(SuccessMessageMixin,generic.UpdateView):
    form_class = AwCouponForm
    template_name = 'admin/coupon/create.html'
    queryset = AwCuponCode.objects.all()

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Coupon update successfully."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Edit Coupon"
        return context


class CouponDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwCuponCode
    template_name = 'admin/coupon/delete.html'
    success_url = reverse_lazy('admin_manage_cupon_code:admin_manage_cupon_code')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete Coupon"
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Coupon remove successfully."