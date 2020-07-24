from django.shortcuts import render,HttpResponseRedirect,HttpResponse,get_object_or_404
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Service_Interests,AwInterestType
from .forms import AwServiceInterestsForm
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

# Create your views here.



@method_decorator(login_required , name="dispatch")
class ManagePerferencesView(SuccessMessageMixin,generic.ListView):
    template_name = 'admin/preferences/index.html'
    queryset = Service_Interests.objects.all().order_by("-id")
    # queryset1 = Wine_Interests.objects.all().order_by("-id")

    def get_context_data(self, *args,**kwargs):
        context  = super(ManagePerferencesView,self).get_context_data(*args,**kwargs)
        context['Page_title'] = "Manage Preferences"
        print(context)
        return context



@method_decorator(login_required , name="dispatch")
class CreatePerferencesView(SuccessMessageMixin,generic.View):
    template_name = 'admin/preferences/create.html'
    form_class = AwServiceInterestsForm
    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'Page_title': "Add Preferences", 'form':form})

    def post(self, request, *args, **kwargs):
        form = AwServiceInterestsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Preferences add successfully.")
            return HttpResponseRedirect(reverse('admin_manage_perferences:perferences'))
        else:
            return render(request, self.template_name, {'form': form,'Page_title':"Add Preferences"})




@method_decorator(login_required , name="dispatch")
class UpdatePerferencesView(SuccessMessageMixin,generic.View):
    template_name = 'admin/preferences/perferences_edit.html'

    def get(self, request, *args, **kwargs):
        perferences_id = self.kwargs.get("id")
        get_perferences_ins = get_object_or_404(Service_Interests, id=perferences_id)
        form = AwServiceInterestsForm(instance=get_perferences_ins)

        return render(request, self.template_name,{'get_perferences_ins':get_perferences_ins,'Page_title': "Edit Preferences", 'form':form})

    def post(self, request, *args, **kwargs):
        perferences_id = self.kwargs.get("id")
        get_perferences_ins = get_object_or_404(Service_Interests, id=perferences_id)
        form = AwServiceInterestsForm(request.POST,instance=get_perferences_ins)
        if form.is_valid():
            form.save()
            messages.info(request, "Service Interests update successfully.")
            return HttpResponseRedirect(reverse('admin_manage_perferences:perferences'))
        else:
            messages.info(request, "Service Interests not updated.")
            return HttpResponseRedirect(reverse('admin_manage_perferences:perferences'))

