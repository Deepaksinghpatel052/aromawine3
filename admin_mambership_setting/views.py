from django.shortcuts import render,get_object_or_404,redirect, HttpResponseRedirect
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import AwMembershipForm
from .models import AwMembership
from django.contrib import messages
from django.urls import reverse
from django.urls import reverse_lazy
from django.template.defaulttags import register
from orders.models import AwOrders
from django.db.models import Sum
from profile_user.models import AwUserInfo
# Create your views here.


@register.filter(name='get_user_membership')
def get_user_membership(user_ins):
    total_order_amount = 0
    get_membership = "No membership"
    if AwOrders.objects.filter(User=user_ins).exists():
        get_order = AwOrders.objects.filter(User=user_ins).aggregate(Sum('Amount'))
        if get_order['Amount__sum']:
            total_order_amount =  int(get_order['Amount__sum'])
    if AwOrders.objects.filter(User=user_ins).exists():
        get_order = AwOrders.objects.filter(User=user_ins).aggregate(Sum('shipping_charge'))
        if get_order['shipping_charge__sum']:
            total_order_amount = total_order_amount +  get_order['shipping_charge__sum']

    if AwMembership.objects.filter(min_price__lte=total_order_amount).filter(max_price__gte=total_order_amount).exists():
        get_membership = get_object_or_404(AwMembership,min_price__lte=total_order_amount,max_price__gte=total_order_amount)
    return get_membership



@register.filter(name='get_userorder_items')
def get_userorder_items(user_ins):
    total_order_Quentity = 0
    get_membership = "No membership"
    if AwOrders.objects.filter(User=user_ins).exists():
        get_order = AwOrders.objects.filter(User=user_ins).aggregate(Sum('Quentity'))
        if get_order['Quentity__sum']:
            total_order_Quentity = get_order['Quentity__sum']
    return total_order_Quentity


@register.filter(name='get_user_number')
def get_user_number(user_ins):
    user_number = ""
    if AwUserInfo.objects.filter(User=user_ins).exists():
        get_user_info = get_object_or_404(AwUserInfo,User=user_ins)
        if get_user_info.Contact_no:
            user_number =  get_user_info.Contact_no
    return user_number


@register.filter(name='get_userorder_amount_cellar')
def get_userorder_amount_cellar(user_ins):
    user_number = ""
    total_order_amount = 0
    if AwOrders.objects.filter(User=user_ins).filter(Order_Type='Caller').exists():
        get_order = AwOrders.objects.filter(User=user_ins).filter(Order_Type='Caller').aggregate(Sum('Amount'))
        if get_order['Amount__sum']:
            total_order_amount = get_order['Amount__sum']
    return total_order_amount


@method_decorator(login_required , name="dispatch")
class ManageMembershipView(SuccessMessageMixin,generic.TemplateView):
    # queryset = AwProducers.objects.all().order_by("-id")
    form_class = AwMembershipForm
    template_name = 'admin/membership/membership.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        queryset = AwMembership.objects.all().order_by("-id")
        return render(request, self.template_name,{'form_class': form, 'Page_title': "Manage Membership", "object": queryset})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        queryset = AwMembership.objects.all().order_by("-id")
        if form.is_valid():
            form.save()
            messages.info(request, "Membership add successfully.")
            return HttpResponseRedirect(reverse('admin_mambership_setting:membership'))
        else:
            return render(request, self.template_name, {'form_class': form,"object":queryset,'Page_title':"Manage Membership"})


@method_decorator(login_required , name="dispatch")
class ManageUpdateView(SuccessMessageMixin,generic.UpdateView):
    form_class = AwMembershipForm
    template_name = 'admin/membership/edit.html'
    queryset = AwMembership.objects.all()
    success_url = reverse_lazy('admin_mambership_setting:membership')

    def get_success_message(self, cleaned_data):
        return "Membership update successfully."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Edit membership"
        return context
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Updated_by = self.request.user
        success_url = reverse_lazy('admin_mambership_setting:membership')
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super(ManageUpdateView, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            messages.error(self.request, form.errors)
            return HttpResponseRedirect(reverse('admin_mambership_setting:membership'))


class MembershipDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwMembership
    template_name = 'admin/membership/delete.html'
    success_url = reverse_lazy('admin_mambership_setting:membership')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete membership"
        return context
    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "membership remove successfully."



