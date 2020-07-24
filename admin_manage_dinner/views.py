from django.shortcuts import render,HttpResponseRedirect,HttpResponse,get_object_or_404
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import AwDinner
from .forms import AwDinnerForm
from datetime import datetime
from datetime import date
from django.urls import reverse_lazy
from django.core.files.base import ContentFile
import base64
# Create your views here.


@method_decorator(login_required , name="dispatch")
class ManageDinnerView(SuccessMessageMixin,generic.ListView):
    queryset = AwDinner.objects.all().order_by("-id")
    template_name = 'admin/dinner/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ManageDinnerView, self).get_context_data(*args, **kwargs)
        return context


@method_decorator(login_required , name="dispatch")
class CreateDinnerView(SuccessMessageMixin,generic.CreateView):
    form_class = AwDinnerForm
    template_name = 'admin/dinner/create.html'

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Dinner add successfully."
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['Page_title'] = "Add Dinner"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Created_by = self.request.user
        self.object.Updated_by = self.request.user
        # print("=================")
        if self.request.POST["dinner_image"]:
            format, imgstr = self.request.POST["dinner_image"].split(';base64,')
            ext = format.split('/')[-1]
            dateTimeObj = datetime.now()
            today_date = date.today()
            set_file_name = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" +str(dateTimeObj.microsecond)
            file_name = set_file_name + "." + ext
            data = ContentFile(base64.b64decode(imgstr), name=file_name)
            self.object.Dinner_Image = data
        # print("===============")
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)


@method_decorator(login_required , name="dispatch")
class DinnerUpdateView(SuccessMessageMixin,generic.UpdateView):
    form_class = AwDinnerForm
    template_name = 'admin/dinner/create.html'
    queryset = AwDinner.objects.all()

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Dinner update successfully."
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['Page_title'] = "Edit Dinner"
        print(context)
        return context
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Updated_by = self.request.user
        # print("=================")
        if self.request.POST["dinner_image"]:
            format, imgstr = self.request.POST["dinner_image"].split(';base64,')
            ext = format.split('/')[-1]
            dateTimeObj = datetime.now()
            today_date = date.today()
            set_file_name = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" +str(dateTimeObj.microsecond)
            file_name = set_file_name + "." + ext
            data = ContentFile(base64.b64decode(imgstr), name=file_name)
            self.object.Dinner_Image = data
        self.object.Updated_date = datetime.now()
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)


class DinnerDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwDinner
    template_name = 'admin/dinner/delete.html'
    success_url = reverse_lazy('admin_manage_dinner:dinner')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete Dinner"
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Dinner remove successfully."