from django.shortcuts import render,HttpResponseRedirect,HttpResponse,get_object_or_404,redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from .forms import AwPaymentMethodForm
from django.urls import reverse
from .models import AwPaymentMethod
from datetime import datetime
from wineproject import settings
from django.contrib import messages
# Create your views here.
class PaymentMethod(generic.TemplateView):
    template_name = "web/user/page/paymentdetails/list.html"
    payment_form = AwPaymentMethodForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Payment Method"
        context['BASE_URL'] = settings.BASE_URL
        get_address = None
        if AwPaymentMethod.objects.filter(Created_by=self.request.user).exists():
            get_address = AwPaymentMethod.objects.filter(Created_by=self.request.user)
        context['object_list'] = get_address
        context['payment_form'] = self.payment_form
        get_payment = None
        if AwPaymentMethod.objects.filter(Created_by=self.request.user).exists():
            get_payment = AwPaymentMethod.objects.filter(Created_by=self.request.user)
        context['get_payment'] = get_payment
        return context

    def post(self, request, *args, **kwargs):
        form = AwPaymentMethodForm(request.POST)
        if form.is_valid():
            payment_ins = form.save(commit=False)
            payment_ins.Created_by=request.user
            payment_ins.save()
            messages.info(request, "Payment method add successfully.")

            return HttpResponseRedirect(reverse('payment_method:payment_method'))
        else:
            messages.error(request, form.errors)
            return render(request, self.template_name, {'payment_form': form, 'Page_title': "Payment Method"})
        
@login_required
def RemovePayment(request,pk):
    if AwPaymentMethod.objects.filter(id=pk).filter(Created_by  = request.user):
        get_instance = get_object_or_404(AwPaymentMethod, id=pk,Created_by  = request.user)
        get_instance.delete()
        messages.info(request, 'payment methodremove successfully')
    else:
        messages.error(request, "payment method is not deleted.")
    return redirect(settings.BASE_URL+"user/payment-details/")