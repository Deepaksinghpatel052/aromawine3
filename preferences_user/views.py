from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from admin_manage_perferences.models import Service_Interests,AwInterestType
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import User_Service_Interests
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate


# Create your views here.


@method_decorator(login_required , name="dispatch")
class UserPreferencesView(SuccessMessageMixin,generic.ListView):
    template_name = "web/user/page/preferences/customer-preference-page.html"
    queryset = Service_Interests.objects.all().order_by("-id")

    def get_context_data(self, *args,**kwargs):
        context  = super(UserPreferencesView,self).get_context_data(*args,**kwargs)
        context['Page_title'] = self.request.user.username + "-update-preference"
        return context


@method_decorator(login_required , name="dispatch")
class UpdateUserPreferencesView(SuccessMessageMixin,generic.ListView):
    template_name = "web/user/page/preferences/customer-preference-page.html"
    queryset = Service_Interests.objects.all().order_by("-id")

    def get_context_data(self, *args,**kwargs):
        context  = super(UpdateUserPreferencesView,self).get_context_data(*args,**kwargs)
        context['Page_title'] = self.request.user.username + "-update-preference"
        return context

    def post(self, request, *args, **kwargs):
        interest_value = request.POST.getlist('serviceInterests[]')
        user_ins = get_object_or_404(User, pk=request.user.id)
        delval = User_Service_Interests.objects.filter(Interested_User=user_ins)
        for delvale in delval:
            perference_user_ins = get_object_or_404(User_Service_Interests, pk=delvale.id)
            perference_user_ins.delete()
        for interest_id in interest_value:
            perference_ins = get_object_or_404(Service_Interests, pk=interest_id)
            perference_name = perference_ins.Service_interests_name
            perferencedata = User_Service_Interests(Service_interests_by_user=perference_name, Interested_User=user_ins, Service_interest=perference_ins)
            perferencedata.save()
        # return render(request, self.template_name, {'Page_title': "Manage Orders"})
        messages.info(request, "Preferences update successfully.")

        return HttpResponseRedirect(reverse('preferences_user:preferenceslist'))





