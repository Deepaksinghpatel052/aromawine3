from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from home.models import AwCmsPaage
from django.views import generic
from .forms import AwCmsPaageForm
from django.urls import reverse_lazy
from datetime import datetime
from datetime import date
from django.core.files.base import ContentFile
import base64
# Create your views here.
@method_decorator(login_required , name="dispatch")
class ManageCustomPage(generic.ListView):
    template_name = "admin/custom_page/index.html"
    queryset = AwCmsPaage.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Manage Custom Page"
        return context

@method_decorator(login_required , name="dispatch")
class CreatePageView(SuccessMessageMixin,generic.CreateView):
    form_class = AwCmsPaageForm
    template_name = 'admin/custom_page/create.html'
    success_url = reverse_lazy('admin_manage_content_page:custom_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Add Page"
        # print(context)
        return context

    def get_success_message(self, cleaned_data):
        # print(cleaned_data)
        return "Page add successfully."

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Created_by = self.request.user
        self.object.Updated_by = self.request.user


        # if self.request.POST["banner_image"]:
        #     format, imgstr = self.request.POST["banner_image"].split(';base64,')
        #     ext = format.split('/')[-1]
        #     dateTimeObj = datetime.now()
        #     today_date = date.today()
        #     set_file_name = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" +str(dateTimeObj.microsecond)
        #     file_name = set_file_name + "." + ext
        #     data = ContentFile(base64.b64decode(imgstr), name=file_name)
        #     self.object.Background_Image = data

        self.object.save()
        form.save()
        return super().form_valid(form)


@method_decorator(login_required , name="dispatch")
class PageUpdateView(SuccessMessageMixin,generic.UpdateView):
    form_class = AwCmsPaageForm
    template_name = 'admin/custom_page/create.html'
    queryset = AwCmsPaage.objects.all()
    success_url = reverse_lazy('admin_manage_content_page:custom_page')

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Page update successfully."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Edit Page"
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
            self.object.Background_Image = data
        # print("===============")
        self.object.Updated_date = datetime.now()
        self.object.save()
        form.save()
        return super().form_valid(form)\


class PageDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwCmsPaage
    template_name = 'admin/custom_page/delete.html'
    success_url = reverse_lazy('admin_manage_content_page:custom_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete "
        return context

    def get_success_message(self, cleaned_data):
        return "Page delete successfully."