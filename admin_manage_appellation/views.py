from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from .models import AwAppellation
from .form import AwAppellationForm
from django.urls import reverse
from django.urls import reverse_lazy
# Create your views here.

@method_decorator(login_required , name="dispatch")
class ManageAppellationView(SuccessMessageMixin,generic.View):
    form_class = AwAppellationForm
    template_name = "admin/appellation/index.html"


    def get(self, request, *args, **kwargs):
        form = self.form_class
        queryset = AwAppellation.objects.all().order_by("-id")
        return render(request, self.template_name, {'form_class': form,'Page_title':"Manage Appellation","object":queryset})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        queryset = AwAppellation.objects.all().order_by("-id")
        if form.is_valid():
            form.save()
            messages.info(request, "Appellation add successfully.")
            return HttpResponseRedirect(reverse('admin_manage_appellation:appellation'))
        else:
            return render(request, self.template_name, {'form_class': form,'Page_title':"Manage Appellation","object":queryset})



@method_decorator(login_required , name="dispatch")
class appellationUpdateView(SuccessMessageMixin,generic.UpdateView):
    form_class = AwAppellationForm
    template_name = 'admin/appellation/edit.html'
    queryset = AwAppellation.objects.all()
    success_url = reverse_lazy('admin_manage_appellation:appellation')

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Appellation update successfully."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Edit appellation"
        print(context)
        return context
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Updated_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super(appellationUpdateView, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            messages.error(self.request, form.errors)
            return HttpResponseRedirect(reverse('admin_manage_appellation:appellation'))

class AppellationDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwAppellation
    template_name = 'admin/appellation/delete.html'
    success_url = reverse_lazy('admin_manage_appellation:appellation')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete Appellation"
        return context
    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Appellation remove successfully."