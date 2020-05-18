from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from .models import AwCountry
from .forms import AwCountryForm
from admin_manage_producer.models import AwSetTo
from datetime import datetime
from datetime import date
from django.urls import reverse_lazy

from django.core.files.base import ContentFile
import base64
# Create your views here.

@method_decorator(login_required , name="dispatch")
class ManageCountryView(SuccessMessageMixin,generic.ListView):
    queryset = AwCountry.objects.all().order_by("-id")
    template_name = 'admin/country/index.html'

    def get_context_data(self, *args,**kwargs):
        context  = super(ManageCountryView,self).get_context_data(*args,**kwargs)
        context['Page_title'] = "Manage Countryes"
        print(context)
        return context


@method_decorator(login_required , name="dispatch")
class CreateCountryView(SuccessMessageMixin,generic.CreateView):
    form_class = AwCountryForm
    template_name = 'admin/country/create.html'


    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Country add successfully."
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['set_to'] = AwSetTo.objects.all()
        context['Page_title'] = "Add Country"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Created_by = self.request.user
        self.object.Updated_by = self.request.user
        # print("=================")
        if self.request.POST["country_image"]:
            format, imgstr = self.request.POST["country_image"].split(';base64,')
            ext = format.split('/')[-1]
            dateTimeObj = datetime.now()
            today_date = date.today()
            set_file_name = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" +str(dateTimeObj.microsecond)
            file_name = set_file_name + "." + ext
            data = ContentFile(base64.b64decode(imgstr), name=file_name)
            self.object.Country_Image = data
        # print("===============")
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)



@method_decorator(login_required , name="dispatch")
class CountryUpdateView(SuccessMessageMixin,generic.UpdateView):
    form_class = AwCountryForm
    template_name = 'admin/country/create.html'
    queryset = AwCountry.objects.all()

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Country update successfully."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Edit Country"
        return context
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Updated_by = self.request.user
        # print("=================")
        if self.request.POST["country_image"]:
            format, imgstr = self.request.POST["country_image"].split(';base64,')
            ext = format.split('/')[-1]
            dateTimeObj = datetime.now()
            today_date = date.today()
            set_file_name = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" +str(dateTimeObj.microsecond)
            file_name = set_file_name + "." + ext
            data = ContentFile(base64.b64decode(imgstr), name=file_name)
            self.object.Country_Image = data
        # print("===============")

        self.object.Updated_date = datetime.now()
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)


class CountryDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwCountry
    template_name = 'admin/country/delete.html'
    success_url = reverse_lazy('admin_manage_country:country')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete Country"
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "country remove successfully."