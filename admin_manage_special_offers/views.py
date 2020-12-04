from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import AwSpecialOffers
from .forms import AwSpecialOffersForm
# Create your views here.

@method_decorator(login_required , name="dispatch")
class ManageSpecialOffer(SuccessMessageMixin,generic.ListView):
    queryset = AwSpecialOffers.objects.all().order_by("-id")
    template_name = "admin/special_offer/special_offer_listy.html"

    def get_context_data(self, *args,**kwargs):
        context  = super(ManageSpecialOffer,self).get_context_data(*args,**kwargs)
        context['Page_title'] = "Manage Special Offer"
        print(context)
        return context

@method_decorator(login_required , name="dispatch")
class CreateSpecialOffereView(SuccessMessageMixin,generic.CreateView):
    form_class = AwSpecialOffersForm
    template_name = 'admin/special_offer/special_offer_create.html'

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Offer add successfully."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Add Special Offer"
        return context


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.Created_by = self.request.user
        self.object.save()
        return super().form_valid(form)

@method_decorator(login_required, name="dispatch")
class OfferUpdateView(SuccessMessageMixin, generic.UpdateView):
    form_class = AwSpecialOffersForm
    template_name = 'admin/special_offer/special_offer_create.html'
    queryset = AwSpecialOffers.objects.all()

    def get_success_message(self, cleaned_data):
        return "Offer update successfully."

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['Page_title'] = "Edit Offers"
        print(context)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)

@method_decorator(login_required, name="dispatch")
class OfferDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AwSpecialOffers
    template_name = 'admin/special_offer/special_offer_delete.html'
    success_url = reverse_lazy('admin_manage_special_offers:special_offer')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Delete Offer"
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Offer remove successfully."
