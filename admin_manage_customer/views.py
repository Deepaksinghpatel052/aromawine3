from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User,auth
from preferences_user.models import User_Service_Interests
from admin_manage_perferences.models import Service_Interests,AwInterestType
from orders.models import AwOrders,AwOrederItem,AwOrderNote

# Create your views here.
@method_decorator(login_required , name="dispatch")
class ManageCustomerView(SuccessMessageMixin,generic.ListView):
    queryset = User.objects.all().order_by("-id")
    template_name = 'admin/customer/customer_list.html'

    def get_context_data(self, *args,**kwargs):
        context  = super(ManageCustomerView,self).get_context_data(*args,**kwargs)
        context['Page_title'] = "Manage Customer"
        print(context)
        return context


@method_decorator(login_required , name="dispatch")
class ManageUserInfoView(SuccessMessageMixin,generic.DetailView):
    template_name = 'admin/customer/customer_info.html'

    def get_context_data(self, *args,**kwargs):
        context  = super(ManageUserInfoView,self).get_context_data(*args,**kwargs)
        context['Page_title'] = "Manage User Info"
        id = self.kwargs.get("id")
        user_prefrence = None

        get_user_info  = None
        if User.objects.filter(id=id):
            get_user_info = get_object_or_404(User,id=id)
        context['get_user_info'] = get_user_info
        if User_Service_Interests.objects.filter(Interested_User__id=id).exists():
            user_prefrence = User_Service_Interests.objects.filter(Interested_User__id=id)
        context['user_prefrence'] = user_prefrence
        print(context)
        return context

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        get_user_ins =  get_object_or_404(User,id=id)
        return User_Service_Interests.objects.filter(Interested_User=get_user_ins)




@method_decorator(login_required , name="dispatch")
class ManagePrefrenceView(SuccessMessageMixin,generic.DetailView):
    template_name = 'admin/customer/customer_prefrenc.html'

    def get_context_data(self, *args,**kwargs):
        context  = super(ManagePrefrenceView,self).get_context_data(*args,**kwargs)
        context['Page_title'] = "Manage Preferences"
        id = self.kwargs.get("id")
        user_prefrence = None

        get_user_info  = None
        if User.objects.filter(id=id):
            get_user_info = get_object_or_404(User,id=id)
        context['get_user_info'] = get_user_info
        if User_Service_Interests.objects.filter(Interested_User__id=id).exists():
            user_prefrence = User_Service_Interests.objects.filter(Interested_User__id=id)
        context['user_prefrence'] = user_prefrence
        print(context)
        return context

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        get_user_ins =  get_object_or_404(User,id=id)
        return User_Service_Interests.objects.filter(Interested_User=get_user_ins)




@method_decorator(login_required , name="dispatch")
class ManageUserOrderHistoryView(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/customer/user_order_info.html'

    def get(self, request, *args, **kwargs):
        queryset = None
        id = self.kwargs.get("id")
        if AwOrders.objects.filter(User__id=id).exists():
            queryset = AwOrders.objects.filter(User__id=id).order_by("-id")
        return render(request, self.template_name, { 'Page_title': "Manage Delivery Orders", 'queryset': queryset})


