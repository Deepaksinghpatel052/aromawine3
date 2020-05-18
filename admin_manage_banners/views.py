from django.shortcuts import render
from django.views import generic
from .models import AwBanners
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
from datetime import date
from .forms import AwBannersForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.files.base import ContentFile
import base64
# Create your views here.
@method_decorator(login_required , name="dispatch")
class ManageBannersView(generic.ListView):
    template_name = "admin/banners/index.html"
    queryset = AwBanners.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Manage Banners"
        return context



@method_decorator(login_required , name="dispatch")
class CreateBannerView(SuccessMessageMixin,generic.CreateView):
    form_class = AwBannersForm
    template_name = 'admin/banners/create.html'
    success_url = reverse_lazy('admin_manage_banners:banners')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Add Banners"
        # print(context)
        return context

    def get_success_message(self, cleaned_data):
        # print(cleaned_data)
        return "Banner add successfully."

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Created_by = self.request.user
        self.object.Updated_by = self.request.user


        if self.request.POST["banner_image"]:
            format, imgstr = self.request.POST["banner_image"].split(';base64,')
            ext = format.split('/')[-1]
            dateTimeObj = datetime.now()
            today_date = date.today()
            set_file_name = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" +str(dateTimeObj.microsecond)
            file_name = set_file_name + "." + ext
            data = ContentFile(base64.b64decode(imgstr), name=file_name)
            self.object.Image = data

        self.object.save()
        form.save()
        return super().form_valid(form)



@method_decorator(login_required , name="dispatch")
class BannersUpdateView(SuccessMessageMixin,generic.UpdateView):
    form_class = AwBannersForm
    template_name = 'admin/banners/create.html'
    queryset = AwBanners.objects.all()
    success_url = reverse_lazy('admin_manage_banners:banners')

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Banner update successfully."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Edit Banner"
        return context
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Updated_by = self.request.user
        # print("=================")
        if self.request.POST["banner_image"]:
            format, imgstr = self.request.POST["banner_image"].split(';base64,')
            ext = format.split('/')[-1]
            dateTimeObj = datetime.now()
            today_date = date.today()
            set_file_name = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" +str(dateTimeObj.microsecond)
            file_name = set_file_name + "." + ext
            data = ContentFile(base64.b64decode(imgstr), name=file_name)
            self.object.Image = data
        # print("===============")
        self.object.Updated_date = datetime.now()
        self.object.save()
        form.save()
        return super().form_valid(form)


class BannersDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwBanners
    template_name = 'admin/banners/delete.html'
    success_url = reverse_lazy('admin_manage_banners:banners')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete Banner"
        return context

    def get_success_message(self, cleaned_data):
        return "Banner update successfully."