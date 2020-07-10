from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from .forms import AwAddressBookForm
from django.urls import reverse_lazy
from .models import AwAddressBook
from datetime import datetime
from wineproject import settings
from django.contrib import messages
# Create your views here.

@method_decorator(login_required , name="dispatch")
class AddressBookList(generic.TemplateView):
    template_name = "web/user/page/addressbook/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Address-book"
        context['BASE_URL'] = settings.BASE_URL
        get_address = None
        if AwAddressBook.objects.filter(User=self.request.user).exists():
            get_address = AwAddressBook.objects.filter(User=self.request.user)
        context['object_list'] = get_address
        return context


@method_decorator(login_required , name="dispatch")
class AddNewAddress(SuccessMessageMixin,generic.CreateView):
    form_class = AwAddressBookForm
    template_name = 'web/user/page/addressbook/create.html'
    success_url = reverse_lazy('addressbook_user:addressbooklist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Add-New-Address"
        return context

    def get_success_message(self, cleaned_data):
        return "Address add successfully."

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.User = self.request.user
        self.object.save()
        form.save()
        return super().form_valid(form)

@method_decorator(login_required , name="dispatch")
class AddressUpdateView(SuccessMessageMixin,generic.UpdateView):
    form_class = AwAddressBookForm
    template_name = 'web/user/page/addressbook/create.html'
    queryset = AwAddressBook.objects.all()
    success_url = reverse_lazy('addressbook_user:addressbooklist')

    def get_success_message(self, cleaned_data):
        return "Address update successfully."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Edit-Address"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Update_Date = datetime.now()
        self.object.save()
        form.save()
        return super().form_valid(form)



@login_required
def RemoveAddress(request,pk):
    if AwAddressBook.objects.filter(id=pk).filter(User = request.user):
        get_instance = get_object_or_404(AwAddressBook, id=pk,User = request.user)
        get_instance.delete()
        messages.info(request, 'Address remove successfully')
    else:
        messages.error(request, "Adress is not deleted.")
    return redirect(settings.BASE_URL+"user/addressbook/")

