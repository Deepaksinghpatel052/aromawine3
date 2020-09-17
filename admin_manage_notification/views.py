from django.shortcuts import render,get_object_or_404,redirect, HttpResponseRedirect
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import AwNotificationForm
from .models import AwNotification
from django.contrib import messages
from django.urls import reverse
from django.urls import reverse_lazy
from datetime import datetime
from django.template.defaulttags import register
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
# Create your views here.


def send_notification(request,pk):
    if AwNotification.objects.filter(id=pk).exists():
        AwNotification.objects.filter(id=pk).update(Send_Status=True,Send_date=datetime.now())
        return JsonResponse({"status":"1","message":"Notification send successfully."})
    else:
        return JsonResponse({"status": "1", "message": "Id is incorrect."})




@method_decorator(login_required , name="dispatch")
class ManageNotificationView(SuccessMessageMixin,generic.TemplateView):
    # queryset = AwProducers.objects.all().order_by("-id")
    form_class = AwNotificationForm
    template_name = 'admin/notification/notification.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        queryset = AwNotification.objects.all().order_by("-id")
        return render(request, self.template_name,{'form_class': form, 'Page_title': "Manage Notification", "object": queryset})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        queryset = AwNotification.objects.all().order_by("-id")
        if form.is_valid():
            notificastion_ins = form.save(commit=False)
            notificastion_ins.Created_by = request.user
            notificastion_ins.save()
            form.save_m2m()
            messages.info(request, "Notification add successfully.")
            return HttpResponseRedirect(reverse('admin_manage_notification:notification'))
        else:
            return render(request, self.template_name, {'form_class': form,"object":queryset,'Page_title':"Manage Membership"})




@method_decorator(login_required , name="dispatch")
class ManageUpdateView(SuccessMessageMixin,generic.UpdateView):
    form_class = AwNotificationForm
    template_name = 'admin/notification/edit.html'
    queryset = AwNotification.objects.all()
    success_url = reverse_lazy('admin_manage_notification:notification')

    def get_success_message(self, cleaned_data):
        return "Notification update successfully."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Edit notification"
        return context
    def form_valid(self, form):
        self.object = form.save(commit=False)
        success_url = reverse_lazy('admin_manage_notification:notification')
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super(ManageUpdateView, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            messages.error(self.request, form.errors)
            return HttpResponseRedirect(reverse('admin_manage_notification:notification'))







class NotificationDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwNotification
    template_name = 'admin/notification/delete.html'
    success_url = reverse_lazy('admin_manage_notification:notification')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete notification"
        return context
    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "notification remove successfully."

