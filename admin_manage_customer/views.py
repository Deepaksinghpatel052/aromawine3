from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User,auth
from preferences_user.models import User_Service_Interests
from admin_manage_perferences.models import Service_Interests,AwInterestType

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
class ManagePrefrenceView(SuccessMessageMixin,generic.DetailView):
    template_name = 'admin/customer/customer_prefrenc.html'

    def get_context_data(self, *args,**kwargs):
        context  = super(ManagePrefrenceView,self).get_context_data(*args,**kwargs)
        context['Page_title'] = "Manage Preferences"
        id = self.kwargs.get("id")
        user_prefrence = None
        if User_Service_Interests.objects.filter(Interested_User__id=id).exists():
            user_prefrence = User_Service_Interests.objects.filter(Interested_User__id=id)
        context['user_prefrence'] = user_prefrence
        print(context)
        return context

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        get_user_ins =  get_object_or_404(User,id=id)
        return User_Service_Interests.objects.filter(Interested_User=get_user_ins)