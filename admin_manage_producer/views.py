from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import AwProducersForm
from .models import AwSetTo,AwProducers
from datetime import datetime
from datetime import date
from django.urls import reverse_lazy
from django.core.files.base import ContentFile
import base64

@method_decorator(login_required , name="dispatch")
class ManageProducerView(SuccessMessageMixin,generic.ListView):
    queryset = AwProducers.objects.all().order_by("-id")
    template_name = 'admin/producer/index.html'

    def get_context_data(self, *args,**kwargs):
        context  = super(ManageProducerView,self).get_context_data(*args,**kwargs)
        print(context)
        return context


@method_decorator(login_required , name="dispatch")
class CreateProducerView(SuccessMessageMixin,generic.CreateView):
    form_class = AwProducersForm
    template_name = 'admin/producer/create.html'

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Producer add successfully."
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['set_to'] = AwSetTo.objects.all()
        context['Page_title'] = "Add Producer"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Created_by = self.request.user
        self.object.Updated_by = self.request.user
        # print("=================")
        if self.request.POST["winnery_image"]:
            format, imgstr = self.request.POST["winnery_image"].split(';base64,')
            ext = format.split('/')[-1]
            dateTimeObj = datetime.now()
            today_date = date.today()
            set_file_name = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" +str(dateTimeObj.microsecond)
            file_name = set_file_name + "." + ext
            data = ContentFile(base64.b64decode(imgstr), name=file_name)
            self.object.Producer_Image = data
        # print("===============")
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)


@method_decorator(login_required , name="dispatch")
class ProducerUpdateView(SuccessMessageMixin,generic.UpdateView):
    form_class = AwProducersForm
    template_name = 'admin/producer/create.html'
    queryset = AwProducers.objects.all()

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Producer update successfully."
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['Page_title'] = "Edit Producer"
        print(context)
        return context
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Updated_by = self.request.user
        # print("=================")
        if self.request.POST["winnery_image"]:
            format, imgstr = self.request.POST["winnery_image"].split(';base64,')
            ext = format.split('/')[-1]
            dateTimeObj = datetime.now()
            today_date = date.today()
            set_file_name = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" +str(dateTimeObj.microsecond)
            file_name = set_file_name + "." + ext
            data = ContentFile(base64.b64decode(imgstr), name=file_name)
            self.object.Producer_Image = data
        self.object.Updated_date = datetime.now()
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)


class GeeksDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwProducers
    template_name = 'admin/producer/delete.html'
    success_url = reverse_lazy('admin_manage_producer:producer')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete Producer"
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Producer remove successfully."