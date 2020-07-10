from django.shortcuts import render,HttpResponseRedirect, HttpResponse,get_object_or_404
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from admin_manage_products.models import AwProductPrice,AwProducts
from orders.serializers import ProductPriceSeriSerializer,AwAddToCardSerializer
from orders.models import AwAddToCard
from django.template.defaulttags import register
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from addressbook_user.forms import AwAddressBookFormUser,AwAddressBookForm
from addressbook_user.models import AwAddressBook
from .models import AwOrders,AwOrederItem
from django.urls import reverse
from django.contrib import messages
from django.db.models import Sum
# Create your views here.

@method_decorator(login_required , name="dispatch")
class CheckOutView(generic.TemplateView):
    template_name = "web/user/page/orders/checkout.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CheckOutView, self).get_context_data(*args, **kwargs)
        context['Page_title'] = "Checkout"
        get_acre_product = None
        if AwAddToCard.objects.filter(User=self.request.user).exists():
            get_acre_product = AwAddToCard.objects.filter(User=self.request.user).order_by("-id")
        context['card_product'] = get_acre_product
        context['address_form'] = AwAddressBookFormUser
        my_address = None
        if AwAddressBook.objects.filter(User=self.request.user).exists():
            my_address = AwAddressBook.objects.filter(User=self.request.user)
        context['my_address'] = my_address
        return context

    def post(self, request, *args, **kwargs):
        if 'old_address' in  request.POST:
            if request.POST["address_id"]:
                addres_id = request.POST["address_id"]
                if AwAddressBook.objects.filter(id=addres_id).exists():
                    get_address_ins = get_object_or_404(AwAddressBook,id=addres_id)
                else:
                    messages.error(request, "Address is incorrect.")
                    return HttpResponseRedirect(reverse('orders:checkout'))
            else:
                messages.error(request, "Address is incorrect.")
                return HttpResponseRedirect(reverse('orders:checkout'))
        else:
            form = AwAddressBookForm(request.POST)

            if form.is_valid():
                self.object = form.save(commit=False)
                self.object.User = request.user
                self.object.save()
                form.save()
                get_address_ins = AwAddressBook.objects.filter(User=request.user).order_by('-id')[0]
            else:
                messages.error(request, form.errors)
                # ================
                context = {}
                context['Page_title'] = "Checkout"
                get_acre_product = None
                if AwAddToCard.objects.filter(User=request.user).exists():
                    get_acre_product = AwAddToCard.objects.filter(User=request.user).order_by("-id")
                context['card_product'] = get_acre_product
                context['address_form'] = AwAddressBookFormUser(request.POST)
                my_address = None
                if AwAddressBook.objects.filter(User=request.user).exists():
                    my_address = AwAddressBook.objects.filter(User=request.user)
                context['my_address'] = my_address
                # ================
                return render(request, self.template_name, context)
                # return HttpResponseRedirect(reverse('orders:checkout'))
        message = request.POST["massage"]
        order_type = request.POST["order_type"]
        payment_type = request.POST["payment_type"]
        quent = 0
        Amount = 0.00
        if AwAddToCard.objects.filter(User=request.user).exists():
            order_data = AwAddToCard.objects.filter(User=self.request.user)
            quent = len(order_data)
            for item in order_data:
                if item.Type == 'Bond':
                    Amount = Amount + (item.Case_Formate.Bond_Cost*item.Quentity)
                if item.Type == 'Retail':
                    Amount = Amount + (item.Case_Formate.Retail_Cost*item.Quentity)
        else:
            messages.error(request, "No Item avelabel in your card.")
            return HttpResponseRedirect(reverse('orders:checkout'))
        add_order = AwOrders(User=request.user,Order_address=get_address_ins,Order_Type=order_type,Notes=message,Quentity=quent,Amount=Amount,Payment_Method=payment_type)
        add_order.save()
        print(add_order)

        for item in order_data:
            if item.Type == 'Bond':
                cost_of_product = item.Case_Formate.Bond_Cost
                total_cost = (item.Case_Formate.Bond_Cost * item.Quentity)
            if item.Type == 'Retail':
                cost_of_product = item.Case_Formate.Retail_Cost
                total_cost= (item.Case_Formate.Retail_Cost * item.Quentity)
            add_item = AwOrederItem(User=request.user,Order_id=add_order,Product=item.Product,Year=item.Year,Type=item.Type,Case_Formate=item.Case_Formate.Bottle,Cost_of_product=cost_of_product,Quentity=item.Quentity,Total_cost=total_cost)
            add_item.save()
        AwAddToCard.objects.filter(User=self.request.user).delete()
        messages.info(request, "Order Plase successfully.")
        return HttpResponseRedirect(reverse('orders:checkout'))

@method_decorator(login_required , name="dispatch")
class OrederVidw(generic.TemplateView):
    template_name = 'web/user/page/orders/order_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(OrederVidw, self).get_context_data(*args, **kwargs)
        context['Page_title'] = "orders"
        get_orders = None
        if AwOrders.objects.filter(User=self.request.user).exists():
            get_orders = AwOrders.objects.filter(User=self.request.user).order_by("-id")
        context['get_orders'] = get_orders
        return context

@method_decorator(login_required , name="dispatch")
class ProoductInfoView(generic.TemplateView):
    template_name = 'web/user/page/orders/order_info.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProoductInfoView, self).get_context_data(*args, **kwargs)
        context['Page_title'] = "order-info"
        order_id = self.kwargs.get("order_id")
        print(order_id)
        get_product = None
        get_sum = None
        if AwOrederItem.objects.filter(User=self.request.user,Order_id__order_id=order_id).exists():
            get_product = AwOrederItem.objects.filter(User=self.request.user,Order_id__order_id=order_id)
            get_sum = AwOrederItem.objects.filter(User=self.request.user,Order_id__order_id=order_id).aggregate(Sum('Total_cost'))
            print(get_sum)
        context['products'] = get_product
        context['total_cost'] = get_sum
        return context


def get_product_list(request):
    user_ins = request.user
    get_product = None
    if AwAddToCard.objects.filter(User=user_ins).exists():
        get_product = AwAddToCard.objects.filter(User=user_ins).order_by("-id")
    data_content = {'get_product':get_product}
    return render(request, 'web/user/page/orders/card_bukate.html', data_content)

@csrf_exempt
def get_my_card_product(request):
    status = 0
    message = ''
    data = {}
    if request.user.username == "":
        message = "User_not_nogin"
    else:
        user_ins = request.user
        if AwAddToCard.objects.filter(User=user_ins).exists():
            get_product = AwAddToCard.objects.filter(User=user_ins).order_by("-id")
            get_data = AwAddToCardSerializer(get_product,many=True)
            data = get_data.data
            status = 1
            message = str(len(get_product))+" Item In card"
        else:
            message = "No Item In card"
    return JsonResponse({"status": status, "message": message,'data':data})




@csrf_exempt
def add_to_card(request):
    status = 0
    message = ""
    if request.method == 'POST':
        user_ins = request.user
        product_id = request.POST['product_id']
        Year = request.POST['Year']
        Type = request.POST['Type']
        Case_Formate_id = request.POST['Case_Formate_id']
        Quentity_set = request.POST['Quentity_set']
        if AwProducts.objects.filter(Product_id=product_id).exists():
            product_ins = get_object_or_404(AwProducts , Product_id=product_id)
            if AwProductPrice.objects.filter(id=Case_Formate_id).exists():
                Case_Formate_ins =get_object_or_404(AwProductPrice , id=Case_Formate_id)
                if  AwAddToCard.objects.filter(User=user_ins).filter(Product=product_ins).filter(Year=Year).filter(Type=Type).filter(Case_Formate=Case_Formate_ins).exists():
                    status = 0
                    message = "This product is already add in your bucket."
                else:
                    add_in_card = AwAddToCard(User=user_ins,Product=product_ins,Year=Year,Type=Type,Case_Formate=Case_Formate_ins,Quentity=Quentity_set)
                    add_in_card.save()
                    status = 1
                    message = "Product add in your bucket."
            else:
                status = 0
                message = "Case_Formate_id is incorrect"
        else:
            status = 0
            message = "product_id is incorrect"
    else:
        status = 0
        message = "Method is incorrect."
    return JsonResponse({"status": status,"message":message})







@register.filter(name='get_product_image')
def get_product_image(product_id):
	# get_videp = VsVideos.objects.filter(Publich_Status=True).order_by("-id").first()
	return product_id

@csrf_exempt
def get_product_price(request):
    if request.method == 'POST':
        data_get_2 = ""
        id =  request.POST['format_id']
        if AwProductPrice.objects.filter(id=id).exists():
            data =get_object_or_404(AwProductPrice , id=id)
            get_data = ProductPriceSeriSerializer(data)
            data_get_2 = get_data.data
    return JsonResponse({"data": data_get_2})