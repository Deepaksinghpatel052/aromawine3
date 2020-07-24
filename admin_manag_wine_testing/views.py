from django.shortcuts import render,HttpResponseRedirect,HttpResponse,get_object_or_404
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import AwTesting
from .forms import AwTestingForm
from datetime import datetime
from datetime import date
from django.urls import reverse_lazy
from django.core.files.base import ContentFile
import base64
# Create your views here.


@method_decorator(login_required , name="dispatch")
class ManageTestingView(SuccessMessageMixin,generic.ListView):
    queryset = AwTesting.objects.all().order_by("-id")
    template_name = 'admin/wine_testing/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ManageTestingView, self).get_context_data(*args, **kwargs)
        return context


@method_decorator(login_required , name="dispatch")
class CreateTestingView(SuccessMessageMixin,generic.CreateView):
    form_class = AwTestingForm
    template_name = 'admin/wine_testing/create.html'

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Testing-wine add successfully."
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['Page_title'] = "Add Testing-Wine"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Created_by = self.request.user
        self.object.Updated_by = self.request.user
        # print("=================")
        if self.request.POST["testing_image"]:
            format, imgstr = self.request.POST["testing_image"].split(';base64,')
            ext = format.split('/')[-1]
            dateTimeObj = datetime.now()
            today_date = date.today()
            set_file_name = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" +str(dateTimeObj.microsecond)
            file_name = set_file_name + "." + ext
            data = ContentFile(base64.b64decode(imgstr), name=file_name)
            self.object.Testing_Image = data
        # print("===============")
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)


@method_decorator(login_required , name="dispatch")
class TestingUpdateView(SuccessMessageMixin,generic.UpdateView):
    form_class = AwTestingForm
    template_name = 'admin/wine_testing/create.html'
    queryset = AwTesting.objects.all()

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Testing-Wine update successfully."
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['Page_title'] = "Edit Testing-Wine"
        print(context)
        return context
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Updated_by = self.request.user
        # print("=================")
        if self.request.POST["testing_image"]:
            format, imgstr = self.request.POST["testing_image"].split(';base64,')
            ext = format.split('/')[-1]
            dateTimeObj = datetime.now()
            today_date = date.today()
            set_file_name = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" +str(dateTimeObj.microsecond)
            file_name = set_file_name + "." + ext
            data = ContentFile(base64.b64decode(imgstr), name=file_name)
            self.object.Testing_Image = data
        self.object.Updated_date = datetime.now()
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)


class TestingDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwTesting
    template_name = 'admin/wine_testing/delete.html'
    success_url = reverse_lazy('admin_manag_wine_testing:testing_wine')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete Testing-Wine"
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Testing-Wine remove successfully."