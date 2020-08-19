from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import AwEvent
from .forms import AwEventForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from datetime import datetime
from datetime import date
from django.core.files.base import ContentFile
import base64

# Create your views here.


@method_decorator(login_required , name="dispatch")
class ManageEventView(generic.ListView):
    queryset = AwEvent.objects.all().order_by("-id")
    template_name = "admin/event/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Manage Event"
        return context


@method_decorator(login_required , name="dispatch")
class CreateEventView(SuccessMessageMixin,generic.CreateView):
    form_class = AwEventForm
    template_name = 'admin/event/create.html'


    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "event add successfully."
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Add event"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Created_by = self.request.user
        self.object.Updated_by = self.request.user
        # print("=================")
        if self.request.POST["event_Image"]:
            format, imgstr = self.request.POST["event_Image"].split(';base64,')
            ext = format.split('/')[-1]
            dateTimeObj = datetime.now()
            today_date = date.today()
            set_file_name = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" +str(dateTimeObj.microsecond)
            file_name = set_file_name + "." + ext
            data = ContentFile(base64.b64decode(imgstr), name=file_name)
            self.object.Event_Image = data
        # print("===============")
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)




@method_decorator(login_required, name="dispatch")
class EventUpdateView(SuccessMessageMixin, generic.UpdateView):
    form_class = AwEventForm
    template_name = 'admin/event/create.html'
    queryset = AwEvent.objects.all()

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Event update successfully."

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['Page_title'] = "Edit Event"

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Updated_by = self.request.user
        # print("=================")
        if self.request.POST["event_Image"]:
            format, imgstr = self.request.POST["event_Image"].split(';base64,')
            ext = format.split('/')[-1]
            dateTimeObj = datetime.now()
            today_date = date.today()
            set_file_name = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year) + "_" + str(
                dateTimeObj.microsecond)
            file_name = set_file_name + "." + ext
            data = ContentFile(base64.b64decode(imgstr), name=file_name)
            self.object.Event_Image = data
        self.object.Updated_date = datetime.now()
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)



class EventDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwEvent
    template_name = 'admin/event/delete.html'
    success_url = reverse_lazy('manage_event:event')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete Event"
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Grape remove successfully."




