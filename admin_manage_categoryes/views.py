from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from .forms import AwCategoryesForm
from datetime import datetime
from datetime import date
from django.core.files.base import ContentFile
import base64
from .models import AwCategory
from django.urls import reverse_lazy
# Create your views here.

@method_decorator(login_required , name="dispatch")
class CreateCategoryView(SuccessMessageMixin,generic.CreateView):
    form_class = AwCategoryesForm
    template_name = 'admin/categoryes/create.html'
    success_url = reverse_lazy('admin_manage_categoryes:catogoryes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Add Categoryes"
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Category add successfully."

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Created_by = self.request.user
        self.object.Updated_by = self.request.user
        print("=================")

        if self.request.POST["category_image"]:
            format, imgstr = self.request.POST["category_image"].split(';base64,')
            ext = format.split('/')[-1]
            dateTimeObj = datetime.now()
            today_date = date.today()
            set_file_name = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" +str(dateTimeObj.microsecond)
            file_name = set_file_name + "." + ext
            data = ContentFile(base64.b64decode(imgstr), name=file_name)
            self.object.Image = data
        print("===============")
        self.object.save()
        form.save()
        return super().form_valid(form)



@method_decorator(login_required , name="dispatch")
class ManageCategoryesView(generic.ListView):
    queryset = AwCategory.objects.all().order_by("-id")
    template_name = "admin/categoryes/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Categoryes"
        return context


@method_decorator(login_required , name="dispatch")
class CategoryUpdateView(SuccessMessageMixin,generic.UpdateView):
    form_class = AwCategoryesForm
    template_name = 'admin/categoryes/create.html'
    queryset = AwCategory.objects.all()
    success_url = reverse_lazy('admin_manage_categoryes:catogoryes')

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Category update successfully."
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['Page_title'] = "Edit Category"
        print("============")
        print(context)
        print("===========")
        return context
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Updated_by = self.request.user
        # print("=================")
        if self.request.POST["category_image"]:
            format, imgstr = self.request.POST["category_image"].split(';base64,')
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



class CategoryDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwCategory
    template_name = 'admin/categoryes/delete.html'
    success_url = reverse_lazy('admin_manage_categoryes:catogoryes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete Category"
        return context
    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Categorye remove successfully."