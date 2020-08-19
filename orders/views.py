from django.shortcuts import render,HttpResponseRedirect, HttpResponse,get_object_or_404,redirect
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
from .models import AwOrders,AwOrederItem,AwOrderNote
from django.urls import reverse
from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from wineproject import settings
from admin_manage_cupon_code.models import AwCuponCode
from datetime import datetime
from datetime import date
# Create your views here.



@csrf_exempt
def check_coupon_code(request):
    status= "0"
    message = "Check coupon"
    data = {}
    if request.method == "POST":
        code = request.POST['coupon_code']
        if AwCuponCode.objects.filter(CouponCode=code).exists():
            get_code_ins = get_object_or_404(AwCuponCode,CouponCode=code)
            if get_code_ins.Valid_from <= datetime.today().date():
                if get_code_ins.Valid_to >= datetime.today().date():
                    status = "1"
                    data["type"]=get_code_ins.Type
                    data["count"]=get_code_ins.Amount
                    message = "Coupon Code applay successgurlly."
                else:
                    message = "Coupon Code is expayer."
            else:
                message = "This code is not usefull at this time."
        else:
            message = "Coupon code is incorrect."
    return JsonResponse({"status": status, "message": message,"data":data})

@csrf_exempt
def update_card(request):
    status = "0"
    message = "Cupon Code is Card update."
    if request.method == "POST":
        ids_set = request.POST.getlist('ids_set[]')
        que_set = request.POST.getlist('que_set[]')
        for id in range(0,len(ids_set)):
            AwAddToCard.objects.filter(id=ids_set[id]).update(Quentity=que_set[id])
    return JsonResponse({"status": status, "message": message})


def remove_product_from_card(request,pk):
    if AwAddToCard.objects.filter(id=pk):
        get_instance = get_object_or_404(AwAddToCard, id=pk)
        get_instance.delete()
        messages.info(request, 'Product remove from card successfully')
    else:
        messages.error(request, "Product is not remove.")
    return redirect(settings.BASE_URL + "user/orders/my-card")

@method_decorator(login_required , name="dispatch")
class MyCardView(generic.TemplateView):
    template_name = "web/user/page/orders/my_card.html"

    def get_context_data(self, *args, **kwargs):
        context = super(MyCardView, self).get_context_data(*args, **kwargs)
        context['Page_title'] = "My-Card"
        card_product  = None
        if self.request.user.username != "":
            user_ins = self.request.user
            if AwAddToCard.objects.filter(User=user_ins).exists():
                card_product = AwAddToCard.objects.filter(User=user_ins).order_by("-id")
        context['card_product'] = card_product
        context['BASE_URL'] = settings.BASE_URL
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        set_coupon_code = request.POST['set_coupon_code']
        set_coupon_type = request.POST['set_coupon_type']
        set_coupon_count = request.POST['set_coupon_count']
        order_type = request.POST["order_type"]
        payment_type = ""
        quent = 0
        Amount = 0.00
        if AwAddToCard.objects.filter(User=request.user).exists():
            order_data = AwAddToCard.objects.filter(User=self.request.user)
            quent = len(order_data)
            for item in order_data:
                if item.Type == 'Bond':
                    Amount = Amount + (item.Case_Formate.Bond_Cost * item.Quentity)
                if item.Type == 'Retail':
                    Amount = Amount + (item.Case_Formate.Retail_Cost * item.Quentity)
        else:
            messages.error(request, "No Item avelabel in your card.")
            return HttpResponseRedirect(reverse('orders:my_card'))
        add_order = AwOrders(User=request.user, Order_Type=order_type,Quentity=quent, order_amount=Amount,Amount=Amount, Payment_Method=payment_type)
        add_order.save()
        if set_coupon_code:
            Cupon_Discount_amount = 0.0
            if set_coupon_type == "P":
                get_persenteg_amoint = (float(Amount) * float(set_coupon_count)) / 100
                Cupon_Discount_amount = float(Amount) - float(get_persenteg_amoint)
            else:
                Cupon_Discount_amount = float(Amount) - float(set_coupon_count)
            AwOrders.objects.filter(order_id=add_order.order_id).update(Use_coupon=True,Cupon_Code=set_coupon_code,Cupon_Discount=get_persenteg_amoint,Amount=Cupon_Discount_amount)
        for item in order_data:
            if item.Type == 'Bond':
                cost_of_product = item.Case_Formate.Bond_Cost
                total_cost = (item.Case_Formate.Bond_Cost * item.Quentity)
            if item.Type == 'Retail':
                cost_of_product = item.Case_Formate.Retail_Cost
                total_cost = (item.Case_Formate.Retail_Cost * item.Quentity)
            add_item = AwOrederItem(User=request.user, Order_id=add_order, Product=item.Product, Year=item.Year,Type=item.Type, Case_Formate_text=item.Case_Formate.Bottle,Case_Formate=item.Case_Formate,Cost_of_product=cost_of_product, Quentity=item.Quentity, Total_cost=total_cost)
            add_item.save()
        AwAddToCard.objects.filter(User=self.request.user).delete()
        # messages.info(request, "Order Plase successfully.")
        return HttpResponseRedirect(reverse('orders:checkout',args=(add_order.order_id,)))



@method_decorator(login_required , name="dispatch")
class CheckOutView(generic.TemplateView):
    template_name = "web/user/page/orders/checkout.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CheckOutView, self).get_context_data(*args, **kwargs)
        context['Page_title'] = "Checkout"
        order_id = self.kwargs.get("order_id")
        get_order_ins = None
        get_acre_product = None
        if AwOrders.objects.filter(order_id=order_id).filter(Order_Status=False).exists():
            get_order_ins = get_object_or_404(AwOrders,order_id=order_id,Order_Status=False)

            if AwOrederItem.objects.filter(User=self.request.user).filter(Order_id=get_order_ins).exists():
                get_acre_product = AwOrederItem.objects.filter(User=self.request.user).filter(Order_id__order_id=order_id)
        context['card_product'] = get_acre_product
        context['get_order_ins'] = get_order_ins
        return context

    def post(self, request, *args, **kwargs):
        order_id = self.kwargs.get("order_id")
        payment_type = request.POST["payment_type"]
        AwOrders.objects.filter(order_id=order_id).update(Order_Status=True,Payment_Status=True,Payment_Method=payment_type,Payment_Date=datetime.now())
        messages.info(request, "Order Place successfully.")
        return HttpResponseRedirect(reverse('orders:checkout',args=(order_id,)))

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
        order_note = None
        get_order_ins = None
        get_acre_product = None
        if AwOrders.objects.filter(order_id=order_id).exists():
            get_order_ins = get_object_or_404(AwOrders,order_id=order_id)
        if AwOrederItem.objects.filter(User=self.request.user,Order_id__order_id=order_id).exists():
            get_product = AwOrederItem.objects.filter(User=self.request.user,Order_id__order_id=order_id)
            get_sum = AwOrederItem.objects.filter(User=self.request.user,Order_id__order_id=order_id).aggregate(Sum('Total_cost'))
            get_sum = get_sum['Total_cost__sum']
            print("===========")
        if AwOrderNote.objects.filter(Order_id__order_id=order_id).filter(Display_Status=True).exists():
            order_note = AwOrderNote.objects.filter(Order_id__order_id=order_id).filter(Display_Status=True).order_by("-id")
        if get_order_ins.Use_coupon:
            get_sum = get_sum - get_order_ins.Cupon_Discount
        context['order_note'] = order_note
        context['products'] = get_product
        context['total_cost'] = get_sum
        context['get_order_ins'] = get_order_ins
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