from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import AwColor
from .forms import AwColorForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
# Create your views here.

@method_decorator(login_required , name="dispatch")
class ManageColorView(generic.ListView):
    queryset = AwColor.objects.all().order_by("-id")
    template_name = "admin/color/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Manage Color"
        return context

@method_decorator(login_required , name="dispatch")
class CreateColorView(SuccessMessageMixin,generic.CreateView):
    form_class = AwColorForm
    template_name = 'admin/color/create.html'
    success_url = reverse_lazy('admin_manage_color:color')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Add Color"
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Category add successfully."


@method_decorator(login_required , name="dispatch")
class ColorUpdateView(SuccessMessageMixin,generic.UpdateView):
    form_class = AwColorForm
    template_name = 'admin/color/create.html'
    queryset = AwColor.objects.all()
    success_url = reverse_lazy('admin_manage_color:color')

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Color update successfully."
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['Page_title'] = "Edit Color"
        print("============")
        print(context)
        print("===========")
        return context


class ColorDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwColor
    template_name = 'admin/color/delete.html'
    success_url = reverse_lazy('admin_manage_color:color')

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Color remove successfully."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete Color"
        return context