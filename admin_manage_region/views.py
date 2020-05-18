from django.shortcuts import render
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import AwRegion
from .forms import AwRegionForm
from datetime import datetime
from datetime import date
from django.urls import reverse_lazy
from django.core.files.base import ContentFile
import base64
# Create your views here.


@method_decorator(login_required , name="dispatch")
class ManageRegionView(SuccessMessageMixin,generic.ListView):
    queryset = AwRegion.objects.all().order_by("-id")
    template_name = 'admin/region/index.html'

    def get_context_data(self, *args,**kwargs):
        context  = super(ManageRegionView,self).get_context_data(*args,**kwargs)
        context['Page_title'] = "Manage Region"
        print(context)
        return context


@method_decorator(login_required , name="dispatch")
class CreateRegionView(SuccessMessageMixin,generic.CreateView):
    form_class = AwRegionForm
    template_name = 'admin/region/create.html'


    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Region add successfully."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Add Region"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Created_by = self.request.user
        self.object.Updated_by = self.request.user
        # print("=================")
        if self.request.POST["Region_Image"]:
            format, imgstr = self.request.POST["Region_Image"].split(';base64,')
            ext = format.split('/')[-1]
            dateTimeObj = datetime.now()
            today_date = date.today()
            set_file_name = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" +str(dateTimeObj.microsecond)
            file_name = set_file_name + "." + ext
            data = ContentFile(base64.b64decode(imgstr), name=file_name)
            self.object.Region_Image = data
        # print("===============")
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class RegionUpdateView(SuccessMessageMixin, generic.UpdateView):
    form_class = AwRegionForm
    template_name = 'admin/region/create.html'
    queryset = AwRegion.objects.all()

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Region update successfully."

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['Page_title'] = "Edit Region"
        print(context)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Updated_by = self.request.user
        # print("=================")
        if self.request.POST["Region_Image"]:
            format, imgstr = self.request.POST["Region_Image"].split(';base64,')
            ext = format.split('/')[-1]
            dateTimeObj = datetime.now()
            today_date = date.today()
            set_file_name = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" + str(
                dateTimeObj.microsecond)
            file_name = set_file_name + "." + ext
            data = ContentFile(base64.b64decode(imgstr), name=file_name)
            self.object.Region_Image = data
        self.object.Updated_date = datetime.now()
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)




class RegionDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwRegion
    template_name = 'admin/region/delete.html'
    success_url = reverse_lazy('admin_manage_region:region')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete Region"
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Region remove successfully."