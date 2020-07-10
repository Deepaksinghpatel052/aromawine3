from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from django.views import generic
from django.urls import reverse
from .models import AwUserInfo
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
# Create your views here.
class UserProfileView(generic.TemplateView):
    template_name = "web/user/page/profile/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = self.request.user.username + "-update-profile"
        return context

class PresonalDetailsView(generic.TemplateView):
    template_name = "web/user/page/profile/presonaldetails.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = self.request.user.username + "-edit-details"
        user_info = None
        title_dist = ['Mr','Mrs','Miss','Ms','Mr & Mrs','Sir','Doctor','Prof','Lord','Lady','Rev','Dame']
        if AwUserInfo.objects.filter(User=self.request.user).exists():
            user_info = get_object_or_404(AwUserInfo,User=self.request.user)
        context['user_info'] = user_info
        context['title_dist'] = title_dist
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        title = request.POST['title']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        contact_no = request.POST['contact_no']
        if AwUserInfo.objects.filter(User=request.user).exists():
            AwUserInfo.objects.filter(User=request.user).update(Title=title,Contact_no=contact_no)
        else:
            add_info = AwUserInfo(User=request.user,Title=title,Contact_no=contact_no)
            add_info.save()
        User.objects.filter(id=request.user.id).update(first_name=first_name,last_name=last_name)
        messages.info(request, 'Information Update successfully.')
        return HttpResponseRedirect(reverse('profile_user:presonaldetails'))


class ChangeEmailView(generic.TemplateView):
    template_name = "web/user/page/profile/chnage_email.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = self.request.user.username + "-chnage-email"
        return context

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        email_2 = request.POST['email_2']
        password = request.POST['password']
        if email ==  email_2:
            username = request.user.username
            password = password
            user_check = authenticate(request, username=username, password=password)
            if user_check is not None:
                User.objects.filter(id=request.user.id).update(email=email_2)
                messages.info(request, 'Email update successfully.')
            else:
                messages.error(request, 'Password is incorrect.')
        else:
            messages.error(request, 'Re-enter email is not match.')
        return HttpResponseRedirect(reverse('profile_user:changeemail'))