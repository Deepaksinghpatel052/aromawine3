from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from .models import AwVarietals
from .forms import AwVarietalsForm
from django.urls import reverse
from django.urls import reverse_lazy
# Create your views here.

@method_decorator(login_required , name="dispatch")
class ManageVarietalsView(SuccessMessageMixin,generic.View):
    form_class = AwVarietalsForm
    template_name = "admin/varietals/index.html"


    def get(self, request, *args, **kwargs):
        form = self.form_class
        queryset = AwVarietals.objects.all().order_by("-id")
        return render(request, self.template_name, {'form_class': form,'Page_title':"Manage varietals","object":queryset})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        queryset = AwVarietals.objects.all().order_by("-id")
        if form.is_valid():
            form.save()
            messages.info(request, "Varietals add successfully.")
            return HttpResponseRedirect(reverse('admin_manage_varietals:varietals'))
        else:
            return render(request, self.template_name, {'form_class': form,"object":queryset,'Page_title':"Manage varietals"})



@method_decorator(login_required , name="dispatch")
class VarietalsUpdateView(SuccessMessageMixin,generic.UpdateView):
    form_class = AwVarietalsForm
    template_name = 'admin/varietals/edit.html'
    queryset = AwVarietals.objects.all()
    success_url = reverse_lazy('admin_manage_varietals:varietals')

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Varietals update successfully."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Edit Varietals"
        print(context)
        return context
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Updated_by = self.request.user
        success_url = reverse_lazy('admin_manage_varietals:varietals')
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super(VarietalsUpdateView, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            messages.error(self.request, form.errors)
            return HttpResponseRedirect(reverse('admin_manage_varietals:varietals'))
class VarietalsDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwVarietals
    template_name = 'admin/varietals/delete.html'
    success_url = reverse_lazy('admin_manage_varietals:varietals')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete varietals"
        return context
    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Vrietals remove successfully."