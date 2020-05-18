from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from .models import AwVintages
from .forms import AwVintagesForm
from django.urls import reverse
from django.urls import reverse_lazy
# Create your views here.

@method_decorator(login_required , name="dispatch")
class ManageVintagesView(SuccessMessageMixin,generic.View):
    form_class = AwVintagesForm
    template_name = "admin/vintages/index.html"


    def get(self, request, *args, **kwargs):
        form = self.form_class
        queryset = AwVintages.objects.all().order_by("-id")
        return render(request, self.template_name, {'form_class': form,'Page_title':"Manage Vintages","object":queryset})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        queryset = AwVintages.objects.all().order_by("-id")
        if form.is_valid():
            form.save()
            messages.info(request, "Vintages add successfully.")
            return HttpResponseRedirect(reverse('admin_manage_Vintages:vintages'))
        else:
            return render(request, self.template_name, {'form_class': form,'Page_title':"Manage Vintages","object":queryset})



@method_decorator(login_required , name="dispatch")
class VintagesUpdateView(SuccessMessageMixin,generic.UpdateView):
    form_class = AwVintagesForm
    template_name = 'admin/vintages/edit.html'
    queryset = AwVintages.objects.all()
    success_url = reverse_lazy('admin_manage_Vintages:vintages')

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Vintages update successfully."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Edit Vintages"
        print(context)
        return context
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Updated_by = self.request.user
        return super().form_valid(form)


class VintagesDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwVintages
    template_name = 'admin/vintages/delete.html'
    success_url = reverse_lazy('admin_manage_Vintages:vintages')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete vintages"
        return context
    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Vintages remove successfully."