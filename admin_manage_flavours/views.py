from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.urls import reverse_lazy
from .forms import AwFlavorsForm
from wine_palate.models import AwWinePalateFlavors,AwWinePalateCategories
# Create your views here.

@method_decorator(login_required , name="dispatch")
class ManageFlavoursView(SuccessMessageMixin,generic.View):
    form_class = AwFlavorsForm
    template_name = "admin/flavours/flavours.html"


    def get(self, request, *args, **kwargs):
        form = self.form_class
        queryset = AwWinePalateFlavors.objects.all().order_by("-id")
        return render(request, self.template_name, {'form_class': form,'Page_title':"Manage Flavours","object":queryset})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        queryset = AwWinePalateFlavors.objects.all().order_by("-id")
        if form.is_valid():
            form.save()
            messages.info(request, "Flavours add successfully.")
            return HttpResponseRedirect(reverse('admin_manage_flavours:flavours'))
        else:
            return render(request, self.template_name, {'form_class': form,"object":queryset,'Page_title':"Manage Flavours"})




class FlavoursDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwWinePalateFlavors
    template_name = 'admin/flavours/delete.html'
    success_url = reverse_lazy('admin_manage_flavours:flavours')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete Flavours"
        return context
    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Flavours remove successfully."



@method_decorator(login_required , name="dispatch")
class FlavoursUpdateView(SuccessMessageMixin,generic.UpdateView):
    form_class = AwFlavorsForm
    template_name = 'admin/flavours/edit.html'
    queryset = AwWinePalateFlavors.objects.all()
    success_url = reverse_lazy('admin_manage_flavours:flavours')

    def get_success_message(self, cleaned_data):
        return "Flavours update successfully."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Edit Flavours"
        return context
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Updated_by = self.request.user
        success_url = reverse_lazy('admin_manage_flavours:flavours')
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super(SizeUpdateView, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            messages.error(self.request, form.errors)
            return HttpResponseRedirect(reverse('admin_manage_flavours:flavours'))
