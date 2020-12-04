from django.shortcuts import render,HttpResponseRedirect, HttpResponse,get_object_or_404,redirect
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from admin_manage_products.models import AwProductPrice,AwProducts
from orders.serializers import ProductPriceSeriSerializer,AwAddToCardSerializer,GetidvalidationAPI,GetAddToCartProductVarifiedSerializers,AwAddToCardSerializer,CheckCouponCodeSerializers
from orders.serializers import CookiesToUserIdValidetorSerializers, AwManageShippingSerializers,AwOrdersSerializers,AwOrederItemSerializers
from orders.models import AwAddToCard
from admin_manage_setting.models import AwManageShipping
from django.template.defaulttags import register
from django.template.loader import render_to_string
from profile_user.models import AwUserInfo
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from addressbook_user.forms import AwAddressBookFormUser,AwAddressBookForm
from addressbook_user.models import AwAddressBook
from addressbook_user.serializers import AwAddressBookSerializare
from .models import AwOrders,AwOrederItem,AwOrderNote
from django.urls import reverse
from manage_event.models import AwEvent
from django.contrib import messages
from rest_framework.views import APIView
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from wineproject import settings
from admin_manage_cupon_code.models import AwCuponCode
from datetime import datetime
from datetime import date
from django.db.models import Q
from rest_framework import generics
from rest_framework import  exceptions
from django.contrib.auth.models import User
# Create your views here.


def do_updaye_cellar_order_status(id):
    if AwOrederItem.objects.filter(id=id).exists():
        get_item_info = get_object_or_404(AwOrederItem,id=id)
        complate_status  = True
        get_all_product_of_this_order = AwOrederItem.objects.filter(Order_id=get_item_info.Order_id)
        for item in get_all_product_of_this_order:
            if item.Quentity > 0:
                complate_status = False
        if complate_status:
            AwOrders.objects.filter(order_id=get_item_info.Order_id.order_id).update(Order_Status_Set='Complete')
    return str(complate_status)



@csrf_exempt
def get_country_id(request):
    address_id = request.POST['address_id']
    address_book_ins = get_object_or_404(AwAddressBook,id=address_id)
    get_data = AwAddressBookSerializare(address_book_ins)
    return JsonResponse(get_data.data)

@csrf_exempt
def get_shipping_charge(request):
    country_id = request.POST['country_id']
    get_shipping_payment = get_object_or_404(AwManageShipping,id=country_id)
    return JsonResponse({"min_ordr_amount":get_shipping_payment.min_ordr_amount,"Shiping_Fees_min_order_amount":get_shipping_payment.Shiping_Fees_min_order_amount})


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
        messages.info(request, 'Product remove from cart successfully')
    else:
        messages.error(request, "Product is not remove.")
    return redirect(settings.BASE_URL + "user/orders/my-cart")


@method_decorator(login_required , name="dispatch")
class OrderInvoiceView(generic.TemplateView):
    template_name = "web/user/page/orders/invoice.html"

    def get_context_data(self, *args, **kwargs):
        context = super(OrderInvoiceView, self).get_context_data(*args, **kwargs)
        context['Page_title'] = "Invoice"
        order_id = self.kwargs.get("order_id")
        print(order_id)
        get_product = None
        get_sum = None
        order_note = None
        get_order_ins = None
        get_acre_product = None
        if AwOrders.objects.filter(order_id=order_id).exists():
            get_order_ins = get_object_or_404(AwOrders, order_id=order_id)
        if AwOrederItem.objects.filter(User=self.request.user, Order_id__order_id=order_id).exists():
            get_product = AwOrederItem.objects.filter(User=self.request.user, Order_id__order_id=order_id)
            get_sum = AwOrederItem.objects.filter(User=self.request.user, Order_id__order_id=order_id).aggregate(
                Sum('Total_cost'))
            get_sum = get_sum['Total_cost__sum']
            print("===========")
        if AwOrderNote.objects.filter(Order_id__order_id=order_id).filter(Display_Status=True).exists():
            order_note = AwOrderNote.objects.filter(Order_id__order_id=order_id).filter(Display_Status=True).order_by(
                "-id")
        if get_order_ins.Use_coupon:
            get_sum = get_sum - get_order_ins.Cupon_Discount
        context['order_note'] = order_note
        context['products'] = get_product
        context['total_cost'] = get_sum
        context['get_order_ins'] = get_order_ins
        context['total_amount_set'] = get_order_ins.Amount + get_order_ins.shipping_charge
        user_info = None
        if AwUserInfo.objects.filter(User=self.request.user).exists():
            user_info = get_object_or_404(AwUserInfo, User=self.request.user)
        context['user_info'] = user_info
        return context

# @method_decorator(login_required , name="dispatch")
class MyCardView(generic.TemplateView):
    template_name = "web/user/page/orders/my_card.html"


    def get_context_data(self, *args, **kwargs):
        context = super(MyCardView, self).get_context_data(*args, **kwargs)
        context['Page_title'] = "My-Cart"
        card_product  = None
        get_cookies = None
        if not self.request.user.is_authenticated:
            user_ins = 0
            if 'aroma_of_wine' in self.request.COOKIES:
                get_cookies = self.request.COOKIES['aroma_of_wine']
                if AwAddToCard.objects.filter(Q(Cookies_id=get_cookies)).exists():
                    card_product = AwAddToCard.objects.filter(Q(Cookies_id=get_cookies)).order_by("-id")
        else:
            user_ins = self.request.user
            if AwAddToCard.objects.filter(Q(User=user_ins)).exists():
                card_product = AwAddToCard.objects.filter(Q(User=user_ins)).order_by("-id")
        context['card_product'] = card_product
        context['BASE_URL'] = settings.BASE_URL
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        set_coupon_code = request.POST['set_coupon_code']
        set_coupon_type = request.POST['set_coupon_type']
        set_coupon_count = request.POST['set_coupon_count']

        set_product_amount = request.POST['set_product_amount']
        set_order_gst = request.POST['set_order_gst']
        order_type = request.POST["order_type"]
        payment_type = ""
        quent = 0
        Amount = 0.00
        if AwAddToCard.objects.filter(User=request.user).exists():
            order_data = AwAddToCard.objects.filter(User=self.request.user)
            quent = len(order_data)
            for item in order_data:
                if item.Order_Type == "Cellar":
                    if item.Type == 'Bond':
                        if item.Case_Formate.Bond_Descount_Cost > 0:
                            Amount = Amount + (item.Case_Formate.Bond_Descount_Cost * item.Quentity)
                        else:
                            Amount = Amount + (item.Case_Formate.Bond_Cost * item.Quentity)
                    if item.Type == 'Retail':
                        if item.Case_Formate.Descount_Cost > 0:
                            Amount = Amount + (item.Case_Formate.Descount_Cost * item.Quentity)
                        else:
                            Amount = Amount + (item.Case_Formate.Retail_Cost * item.Quentity)
                elif item.Order_Type == "Delivered":
                    # if item.order_item_id.Order_id.Payment_Status:
                    #     Amount  = Amount + 0.0
                    # else:
                    Amount = Amount + (item.Old_Cost * item.Quentity)
                else:
                    Amount = Amount + (item.Event_Ticket.ticket_price * item.Quentity)
        else:
            messages.error(request, "No Item avelabel in your card.")
            return HttpResponseRedirect(reverse('orders:my_card'))
        add_order = AwOrders(User=request.user, Order_Type=order_type,Quentity=quent,Order_Product_Amount=set_product_amount,Order_Gst_Amount=set_order_gst, order_amount=Amount,Amount=Amount, Payment_Method=payment_type)
        add_order.save()
        if set_coupon_code:
            Cupon_Discount_amount = 0.0
            if set_coupon_type == "P":
                get_persenteg_amoint = (float(Amount) * float(set_coupon_count)) / 100
                Cupon_Discount_amount = float(Amount) - float(get_persenteg_amoint)
            else:
                get_persenteg_amoint = float(set_coupon_count)
                Cupon_Discount_amount = float(Amount) - float(set_coupon_count)
            AwOrders.objects.filter(order_id=add_order.order_id).update(Use_coupon=True,Cupon_Code=set_coupon_code,Cupon_Discount=get_persenteg_amoint,Amount=Cupon_Discount_amount)

        for item in order_data:
            if item.Order_Type == "Cellar":

                set_gst = item.Case_Formate.GST
                set_duty = item.Case_Formate.Duty
                if item.Type == 'Bond':
                    if item.Case_Formate.Bond_Descount_Cost > 0:
                        cost_of_product = item.Case_Formate.Bond_Descount_Cost
                        total_cost = (item.Case_Formate.Bond_Descount_Cost * item.Quentity)
                    else:
                        cost_of_product = item.Case_Formate.Bond_Cost
                        total_cost = (item.Case_Formate.Bond_Cost * item.Quentity)
                if item.Type == 'Retail':
                    if item.Case_Formate.Descount_Cost > 0:
                        cost_of_product = item.Case_Formate.Descount_Cost
                        total_cost = (item.Case_Formate.Descount_Cost * item.Quentity)
                    else:
                        cost_of_product = item.Case_Formate.Retail_Cost
                        total_cost = (item.Case_Formate.Retail_Cost * item.Quentity)
            elif item.Order_Type == "Delivered":
                cost_of_product = item.Old_Cost
                total_cost = (item.Old_Cost * item.Quentity)
                set_gst = item.order_item_id.Gst
                set_duty = item.order_item_id.Duty
            else:
                set_gst = 0
                set_duty = 0
                cost_of_product = item.Event_Ticket.ticket_price
                total_cost = (item.Event_Ticket.ticket_price * item.Quentity)

            Case_Formate_text_set = None
            if item.Case_Formate:
                Case_Formate_text_set = item.Case_Formate.Bottle
            add_item = AwOrederItem(User=request.user, Gst=set_gst,Duty=set_duty, Order_id=add_order, Product_Cellar=item.Product_Cellar,Product_Delivered=item.Product_Delivered,Event_Ticket=item.Event_Ticket, Year=item.Year,Type=item.Type, Case_Formate_text=Case_Formate_text_set,Case_Formate=item.Case_Formate,Cost_of_product=cost_of_product, Quentity=item.Quentity,Order_Quentity=item.Quentity, Total_cost=total_cost)
            add_item.save()
        # AwAddToCard.objects.filter(User=self.request.user).delete()
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
                get_acre_product = AwOrederItem.objects.filter(User=self.request.user).filter(Order_id__order_id=order_id).order_by("-id")
        context['card_product'] = get_acre_product
        context['get_order_ins'] = get_order_ins

        context['address_form'] = AwAddressBookFormUser
        my_address = None
        if AwAddressBook.objects.filter(User=self.request.user).exists():
            my_address = AwAddressBook.objects.filter(User=self.request.user)
        context['my_address'] = my_address

        if AwUserInfo.objects.filter(User=self.request.user).exists():
            user_info = get_object_or_404(AwUserInfo, User=self.request.user)
        context['user_info'] = user_info

        return context

    def post(self, request, *args, **kwargs):
        order_id = self.kwargs.get("order_id")
        order_data = get_object_or_404(AwOrders, order_id=order_id)
        payment_type = request.POST["payment_type"]

        get_address_ins = None

        context = {}
        context['Page_title'] = "Checkout"
        my_address = None
        if AwAddressBook.objects.filter(User=request.user).exists():
            my_address = AwAddressBook.objects.filter(User=request.user)
        context['my_address'] = my_address
        context['address_form'] = AwAddressBookFormUser

        get_order_ins = None
        get_acre_product = None
        if AwOrders.objects.filter(order_id=order_id).filter(Order_Status=False).exists():
            get_order_ins = get_object_or_404(AwOrders, order_id=order_id, Order_Status=False)

            if AwOrederItem.objects.filter(User=self.request.user).filter(Order_id=get_order_ins).exists():
                get_acre_product = AwOrederItem.objects.filter(User=self.request.user).filter(
                    Order_id__order_id=order_id)
        context['card_product'] = get_acre_product
        context['get_order_ins'] = get_order_ins
        if order_data.Order_Type == 'Delivered':
            payment_type = "Payment Done By Caller"
            if 'old_address' in request.POST:
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
                    return render(request, self.template_name, context)
            else:
                if request.POST["address_id"]:
                    addres_id = request.POST["address_id"]
                    if AwAddressBook.objects.filter(id=addres_id).exists():
                        get_address_ins = get_object_or_404(AwAddressBook, id=addres_id)
                    else:
                        messages.error(request, "Address is incorrect.")
                        return render(request, self.template_name, context)
                else:
                    messages.error(request, "Address is incorrect.")
                    return render(request, self.template_name, context)


        if get_order_ins.Order_Type == 'Delivered':
            shipping_payment_type = request.POST["payment_type"]
            shipping_charge = request.POST["shipping_charge"]
            shipping_Payment_Status_status = True
        else:
            shipping_payment_type = ""
            shipping_charge = 0
            shipping_Payment_Status_status = False


        message = request.POST["massage"]
        AwOrders.objects.filter(order_id=order_id).update(shipping_charge=shipping_charge, order_place=True, Order_Status=True,Payment_Status=True,Payment_Method=payment_type,shipping_Payment_Status=shipping_Payment_Status_status,shipping_Payment_Method=shipping_payment_type,Payment_Date=datetime.now(),Order_address=get_address_ins)

        # ==========================remive product from caller when order is develover===================================
        get_product = AwOrederItem.objects.filter(User=self.request.user).filter(Order_id__order_id=order_id)

        if AwOrders.objects.filter(User=self.request.user).filter(Order_Type='Caller').exists():
            get_old_caller_order = AwOrders.objects.filter(User=self.request.user).filter(Order_Type='Caller')

            for items in get_product:
                if AwOrederItem.objects.filter(Order_id__in=get_old_caller_order).filter(Product_Cellar=items.Product_Delivered).exists():
                    get_caller = AwOrederItem.objects.filter(Order_id__in=get_old_caller_order).filter(Product_Cellar=items.Product_Delivered)
                    for item_get in get_caller:
                        quentity = item_get.Quentity - items.Quentity
                        if quentity <= 0:
                            quentity = 0
                        AwOrederItem.objects.filter(id=item_get.id).update(Quentity=quentity)
                        do_updaye_cellar_order_status(item_get.id)
        # ==========================remive product from caller when order is develover===================================

        if order_data.Order_Type == 'Caller':
            if AwAddToCard.objects.filter(User=self.request.user).exists():
                get_add_to_cart_order = AwAddToCard.objects.filter(User=self.request.user)
                for items in get_add_to_cart_order:
                    product = items.Product_Cellar
                    product_price = items.Case_Formate
                    Quentity  = items.Quentity
                    Type = items.Type
                    if AwProductPrice.objects.filter(id=items.Case_Formate.id).exists():
                        get_ins = get_object_or_404(AwProductPrice,id=items.Case_Formate.id)
                        if items.Type == 'Retail':
                            get_old_que = get_ins.Retail_Stock
                            new  = get_ins.Retail_Stock - items.Quentity
                            AwProductPrice.objects.filter(id=items.Case_Formate.id).update(Retail_Stock=new)
                        else:
                            get_old_que = get_ins.Bond_Stock
                            new = get_ins.Bond_Stock - items.Quentity
                            AwProductPrice.objects.filter(id=items.Case_Formate.id).update(Bond_Stock=new)

        AwAddToCard.objects.filter(User=self.request.user).delete()
        messages.info(request, "Your Order has placed Successfully.")

        # if AwOrders.objects.filter(User=request.user).filter(Order_Type='Caller')


        # return HttpResponseRedirect(reverse('orders:orders',args=(order_id,)))
        return HttpResponseRedirect(reverse('orders:orders'))

@method_decorator(login_required , name="dispatch")
class OrederVidw(generic.TemplateView):
    template_name = 'web/user/page/orders/order_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(OrederVidw, self).get_context_data(*args, **kwargs)
        context['Page_title'] = "orders"
        get_orders = None
        if AwOrders.objects.filter(User=self.request.user).filter(order_place=True).exists():
            get_orders = AwOrders.objects.filter(User=self.request.user).filter(order_place=True).order_by("-id")
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
        context['total_order'] = get_order_ins.Amount+get_order_ins.shipping_charge
        user_info = None
        if AwUserInfo.objects.filter(User=self.request.user).exists():
            user_info = get_object_or_404(AwUserInfo, User=self.request.user)
        context['user_info'] = user_info
        return context


def get_product_list(request):
    get_cookies = None
    get_product = None
    if not request.user.is_authenticated:
        user_ins = 0
        if 'aroma_of_wine' in request.COOKIES:
            get_cookies = request.COOKIES['aroma_of_wine']
            if AwAddToCard.objects.filter(Q(Cookies_id=get_cookies)).exists():
                get_product = AwAddToCard.objects.filter(Q(Cookies_id=get_cookies)).order_by("-id")
    else:
        user_ins = request.user
        if AwAddToCard.objects.filter(Q(User=user_ins)).exists():
            get_product = AwAddToCard.objects.filter(Q(User=user_ins)).order_by("-id")
    data_content = {'get_product':get_product}
    return render(request, 'web/user/page/orders/card_bukate.html', data_content)

@csrf_exempt
def get_my_card_product(request):
    status = 0
    message = ''
    data = {}
    get_cookies = None
    if not request.user.is_authenticated:
        user_ins = 0
        if 'aroma_of_wine' in request.COOKIES:
            get_cookies = request.COOKIES['aroma_of_wine']
            if AwAddToCard.objects.filter(Q(Cookies_id=get_cookies)).exists():
                get_product = AwAddToCard.objects.filter(Q(Cookies_id=get_cookies)).order_by("-id")
                get_data = AwAddToCardSerializer(get_product, many=True)
                data = get_data.data
                status = 1
                message = str(len(get_product)) + " Item In card"
        else:
            message = "No Item In card"
    else:
        user_ins = request.user
        if AwAddToCard.objects.filter(Q(User=user_ins)).exists():
            get_product = AwAddToCard.objects.filter(Q(User=user_ins)).order_by("-id")
            get_data = AwAddToCardSerializer(get_product, many=True)
            data = get_data.data
            status = 1
            message = str(len(get_product)) + " Item In card"
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
        order_type = request.POST['order_type']

        order_id = request.POST['order_id']
        event_id = request.POST['event_id']
        # =========================== Set Order Type Start ===================
        order_type_set = "Cellar"
        set_item_type = "Product"
        if order_type == "c":
            order_type_set = "Cellar"
        if order_type == "d":
            order_type_set = "Delivered"

        if order_type == "t":
            set_item_type = "tickets"
            order_type_set = "Tickets"
        # =========================== Set Order Type End ===================
        Order_Type = order_type_set


        product_ins = None
        product_order_item_ins = None
        event_ins = None
        Case_Formate_ins = None
        product_order_item_ins_all_data = None
        Cost = 0
        if order_type == "c":
            if AwProducts.objects.filter(Product_id=product_id).exists():
                product_ins = get_object_or_404(AwProducts, Product_id=product_id)
                if AwProductPrice.objects.filter(id=Case_Formate_id).exists():
                    Case_Formate_ins = get_object_or_404(AwProductPrice, id=Case_Formate_id)
                    status = 1
                else:
                    status = 0
                    message = "Case_Formate_id is incorrect caller"
            else:
                status = 0
                message = "product_id is incorrect caller"

        if order_type == "d":
            if Case_Formate_id:
                if AwProductPrice.objects.filter(id=Case_Formate_id).exists():
                    Case_Formate_ins = get_object_or_404(AwProductPrice, id=Case_Formate_id)
                    status = 1
                    if AwOrederItem.objects.filter(Product_Cellar__Product_id=product_id).filter(
                            Order_id__id=order_id).filter(Year=Year).filter(Type=Type).filter(
                            Case_Formate=Case_Formate_ins).exists():
                        product_order_item_ins_all_data = get_object_or_404(AwOrederItem,
                                                                            Product_Cellar__Product_id=product_id,
                                                                            Order_id__id=order_id, Year=Year, Type=Type,
                                                                            Case_Formate=Case_Formate_ins)
                        product_order_item_ins = product_order_item_ins_all_data.Product_Cellar
                        Cost = product_order_item_ins_all_data.Cost_of_product
                    else:
                        status = 0
                        message = "product_id is incorrect deleverd"

                else:
                    status = 0
                    message = "Case_Formate_id is incorrect delivery."

            else:
                status = 0
                message = "Case Formate is not available."


        if order_type == "t":
            if AwEvent.objects.filter(id=event_id).exists():
                event_ins = get_object_or_404(AwEvent, id=event_id)

                Cost = event_ins.ticket_price
                status = 1
            else:
                status = 0
                message = "event_id is incorrect deleverd"

        if status == 1:
            status = 0
            # get_cookies = "test"
            if not request.user.is_authenticated:
                user_ins = None
                get_cookies = request.COOKIES['aroma_of_wine']
            else:
                get_cookies = str(datetime.now())
            if AwAddToCard.objects.filter(Q(User=user_ins) | Q(Cookies_id=get_cookies)).exists():
                get_filst_item_ins = AwAddToCard.objects.filter(Q(User=user_ins) | Q(Cookies_id=get_cookies)).first()
                if get_filst_item_ins.Order_Type == order_type_set:
                    if  AwAddToCard.objects.filter(Q(User=user_ins) | Q(Cookies_id=get_cookies)).filter(Product_Cellar=product_ins).filter(Product_Delivered=product_order_item_ins).filter(Event_Ticket=event_ins).filter(Year=Year).filter(Type=Type).filter(Case_Formate=Case_Formate_ins).exists():
                        status = 0
                        message = "This "+set_item_type+" is already add in your bucket."
                    else:
                        add_in_card = AwAddToCard(User=user_ins,Cookies_id=get_cookies, order_item_id=product_order_item_ins_all_data, Old_Cost=Cost, Product_Cellar=product_ins,
                                                  Product_Delivered=product_order_item_ins, Event_Ticket=event_ins,
                                                  Year=Year, Type=Type, Case_Formate=Case_Formate_ins,
                                                  Quentity=Quentity_set, Order_Type=order_type_set)
                        add_in_card.save()
                        status = 1
                        # message =
                        if Order_Type == 't':
                            message = str(Order_Type)+" add in your bucket."
                        else:
                            if order_type_set == 'Delivered':
                                order_type_set = 'Delivery'
                            message = "Wine added for " + order_type_set + ", to the basket"
                else:
                    status = 0
                    message = "You can add only one type "+set_item_type+" ("+str(get_filst_item_ins.Order_Type)+")."
            else:
                add_in_card = AwAddToCard(User=user_ins,Cookies_id=get_cookies,Old_Cost=Cost,order_item_id=product_order_item_ins_all_data, Product_Cellar=product_ins,Product_Delivered=product_order_item_ins,Event_Ticket=event_ins, Year=Year, Type=Type,Case_Formate=Case_Formate_ins, Quentity=Quentity_set, Order_Type=order_type_set)
                add_in_card.save()
                status = 1
                if Order_Type == 't':
                    message = str(Order_Type) + " add in your bucket."
                else:
                    if order_type_set == 'Delivered':
                        order_type_set = 'Delivery'
                    message = "Wine added for " + order_type_set + ", to the basket"
    else:
        status = 0
        message = "Method is incorrect."
    return JsonResponse({"status": status, "message": message})

    #     if AwProducts.objects.filter(Product_id=product_id).exists():
    #         product_ins = get_object_or_404(AwProducts , Product_id=product_id)
    #         if AwProductPrice.objects.filter(id=Case_Formate_id).exists():
    #             Case_Formate_ins =get_object_or_404(AwProductPrice , id=Case_Formate_id)
    #             if  AwAddToCard.objects.filter(User=user_ins).filter(Product=product_ins).filter(Year=Year).filter(Type=Type).filter(Case_Formate=Case_Formate_ins).exists():
    #                 status = 0
    #                 message = "This product is already add in your bucket."
    #             else:
    #                 add_in_card = AwAddToCard(User=user_ins,Product=product_ins,Year=Year,Type=Type,Case_Formate=Case_Formate_ins,Quentity=Quentity_set,order_type='')
    #                 add_in_card.save()
    #                 status = 1
    #                 message = "Product add in your bucket."
    #         else:
    #             status = 0
    #             message = "Case_Formate_id is incorrect"
    #     else:
    #         status = 0
    #         message = "product_id is incorrect"
    # else:
    #     status = 0
    #     message = "Method is incorrect."
    # return JsonResponse({"status": status,"message":message})




@register.filter(name='get_product_image')
def get_product_image(product_id):
	# get_videp = VsVideos.objects.filter(Publich_Status=True).order_by("-id").first()
	return product_id


@register.filter(name='multiply_of_prodiuct_amount_quentity')
def multiply_of_prodiuct_amount_quentity(amount,quentity):
	# get_videp = VsVideos.objects.filter(Publich_Status=True).order_by("-id").first()
	return amount*quentity


@register.filter(name='get_amount_without_persentage')
def get_amount_without_persentage(amount,persentage):
    amount = amount
    persentage_amount = (amount*persentage)/100
    amount_withoput_persentage = amount - persentage_amount
    return amount_withoput_persentage

@register.filter(name='get_persentage_amount')
def get_persentage_amount(amount,persentage):
    amount = amount
    persentage_amount = (amount * persentage) / 100
    return persentage_amount


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

# =====================================================================================================================================

class add_to_card_api(APIView):

    def post(self, request):
        status = 0
        message = ""
        data_response = {}
        serializer = True
        if request.data['order_type'] != "":
            user = request.data['User_id']
            Cookies_id = request.data['Cookies_id']
            get_data = {"user_ins": user}
            serializer = GetidvalidationAPI(data=get_data)
            serializer.is_valid(raise_exception=True)
            user_ins = serializer.validated_data
            product_id = request.data['product_id']
            Year = request.data['Year']
            Type = request.data['Type']
            Case_Formate_id = request.data['Case_Formate_id']
            Quentity_set = request.data['Quentity_set']
            order_type = request.data['order_type']
            order_id = request.data['order_id']
            event_id = request.data['event_id']

            # =========================== Set Order Type Start ===================
            order_type_set = "Cellar"
            set_item_type = "Product"
            if order_type == "c":
                order_type_set = "Cellar"

            if order_type == "d":
                order_type_set = "Delivered"

            if order_type == "t":
                set_item_type = "tickets"
                order_type_set = "Tickets"

            # =========================== Set Order Type End ===================
            product_ins = None
            product_order_item_ins = None
            event_ins = None
            Case_Formate_ins = None
            product_order_item_ins_all_data = None
            Cost = 0
            if order_type == "c":
                if AwProducts.objects.filter(Product_id=product_id).exists():
                    product_ins = get_object_or_404(AwProducts, Product_id=product_id)

                    if AwProductPrice.objects.filter(id=Case_Formate_id).exists():
                        Case_Formate_ins = get_object_or_404(AwProductPrice, id=Case_Formate_id)
                        status = 1

                    else:
                        status = 0
                        message = "Case_Formate_id is incorrect caller"
                else:
                    status = 0
                    message = "product_id is incorrect caller"

            if order_type == "d":
                if AwOrederItem.objects.filter(Product_Cellar__Product_id=product_id).filter(Order_id__id=order_id).filter(Year=Year).exists():
                    product_order_item_ins_all_data = get_object_or_404(AwOrederItem,Product_Cellar__Product_id=product_id,Order_id__id=order_id, Year=Year)
                    product_order_item_ins = product_order_item_ins_all_data.Product_Cellar
                    Cost = product_order_item_ins_all_data.Cost_of_product
                    if AwProductPrice.objects.filter(id=Case_Formate_id).exists():
                        Case_Formate_ins = get_object_or_404(AwProductPrice, id=Case_Formate_id)
                        status = 1
                    else:
                        status = 0
                        message = "Case_Formate_id is incorrect caller"
                else:
                    status = 0
                    message = "product_id is incorrect deleverd"
            if order_type == "t":
                if AwEvent.objects.filter(id=event_id).exists():
                    event_ins = get_object_or_404(AwEvent, id=event_id)
                    Cost = event_ins.ticket_price
                    status = 1
                else:
                    status = 0
                    message = "event_id is incorrect deleverd"
            #         ====================================================
            if not user_ins:
                user_ins = None
                if request.data['Cookies_id'] == "":
                    status = 0
                    message = "Please send me Cookies_id/User_id."
                else:
                    get_cookies = request.data['Cookies_id']
            else:
                get_cookies = str(datetime.now())


            if Year == "":
                status = 0
                message = "Year is required"
            if Type == "":
                status = 0
                message = "Type is required"
            if status == 1:
                status = 0

                if AwAddToCard.objects.filter(Q(User=user_ins) | Q(Cookies_id=get_cookies)).exists():
                    get_filst_item_ins = AwAddToCard.objects.filter(Q(User=user_ins) | Q(Cookies_id=get_cookies)).first()
                    if get_filst_item_ins.Order_Type == order_type_set:
                        if AwAddToCard.objects.filter(Q(User=user_ins) | Q(Cookies_id=get_cookies)).filter(Product_Cellar=product_ins).filter(Product_Delivered=product_order_item_ins).filter(Event_Ticket=event_ins).filter(Year=Year).filter(Type=Type).filter(Case_Formate=Case_Formate_ins).exists():
                            status = 0
                            message = "This " + set_item_type + " is already add in your bucket."
                        else:
                            add_in_card = AwAddToCard(User=user_ins, Cookies_id=get_cookies,
                                                      order_item_id=product_order_item_ins_all_data, Old_Cost=Cost,
                                                      Product_Cellar=product_ins,
                                                      Product_Delivered=product_order_item_ins, Event_Ticket=event_ins,
                                                      Year=Year, Type=Type, Case_Formate=Case_Formate_ins,
                                                      Quentity=Quentity_set, Order_Type=order_type_set)
                            add_in_card.save()
                            if order_type == 't':
                                message = str(order_type) + " add in your bucket."
                            else:
                                if order_type_set == 'Delivered':
                                    order_type_set = 'Delivery'
                                message = "Wine added for " + order_type_set + ", to the basket"
                    else:
                        status = 0
                        message = "You can add only one type " + set_item_type + " (" + str(get_filst_item_ins.Order_Type) + ")."
                else:
                    add_in_card = AwAddToCard(User=user_ins, Cookies_id=get_cookies, Old_Cost=Cost,
                                              order_item_id=product_order_item_ins_all_data, Product_Cellar=product_ins,
                                              Product_Delivered=product_order_item_ins, Event_Ticket=event_ins,
                                              Year=Year, Type=Type, Case_Formate=Case_Formate_ins,
                                              Quentity=Quentity_set, Order_Type=order_type_set)
                    add_in_card.save()
                    status = 1
                    if order_type == 't':
                        message = str(Order_Type) + " add in your bucket."
                    else:
                        if order_type_set == 'Delivered':
                            order_type_set = 'Delivery'
                        message = "Wine added for " + order_type_set + ", to the basket"
        else:
            message = "Add this order_type (c=cellar,d=Delivery,t=tickets)"
        return Response({"status": status, "message": message})

# =================================================================================================================

class get_my_card_product_api(APIView):

    def post(self, request):
        status = 0
        message = ""
        serializer = GetAddToCartProductVarifiedSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        get_serilige_valide_data = serializer.validated_data
        data = {}
        if get_serilige_valide_data['user_ins']:
            if AwAddToCard.objects.filter(User=get_serilige_valide_data['user_ins']).exists():
                get_datat_res  = AwAddToCard.objects.filter(User=get_serilige_valide_data['user_ins'])
                het_data_seri = AwAddToCardSerializer(get_datat_res, many=True)
                data  = het_data_seri.data
                status = 1
        else:
            if AwAddToCard.objects.filter(Cookies_id=get_serilige_valide_data['Cookies_id']).exists():
                get_datat_res  = AwAddToCard.objects.filter(Cookies_id=get_serilige_valide_data['Cookies_id'])
                het_data_seri = AwAddToCardSerializer(get_datat_res, many=True)
                data  = het_data_seri.data
                status = 1
        # AwAddToCardSerializer
        return Response({"status": status, "message": message,"data":data}, status=200)


class remove_product_from_card_api(APIView):

    def post(self,request):
        status = 0
        message = ""
        if "card_product_id" in request.data:
            if request.data['card_product_id']:
                if AwAddToCard.objects.filter(id=request.data['card_product_id']).exists():
                    AwAddToCard.objects.filter(id=request.data['card_product_id']).delete()
                    message = "product remove from your cart."
                    status = 1
                else:
                    mes = "Your card_product_id is incorrected."
                    raise exceptions.ValidationError(mes)
            else:
                mes = "Your card_product_id is required."
                raise exceptions.ValidationError(mes)
        else:
            mes = "Your card_product_id is required."
            raise exceptions.ValidationError(mes)
        return Response({"status": status, "message": message}, status=200)

class update_card_api(APIView):

    def post(self,request):
        status = 0
        message = ""
        ids = request.data['ids']
        quentity = request.data['quentity']
        i=0
        for id in  ids:
            if AwAddToCard.objects.filter(id=id).exists():
                AwAddToCard.objects.filter(id=id).update(Quentity=quentity[i])
            i = i+1
        status = "1"
        message = "Cart update successfully"
        return Response({"status": status, "message": message}, status=200)


class check_coupon_code_api(APIView):

    def post(self, request):
        serializer = CheckCouponCodeSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        get_serilige_valide_data = serializer.validated_data
        return Response(get_serilige_valide_data, status=200)

class cookies_to_user_id(APIView):

    def post(self, request):
        serializer = CookiesToUserIdValidetorSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        get_serilige_valide_data = serializer.validated_data
        return Response(get_serilige_valide_data, status=200)

class get_product_price_api(APIView):

    def post(self, request):
        data_get_2 = ""
        status = 0
        message = ""
        if 'format_id' in request.data:
            id = request.data['format_id']
            if id:
                if AwProductPrice.objects.filter(id=id).exists():
                    data = get_object_or_404(AwProductPrice, id=id)
                    get_data = ProductPriceSeriSerializer(data)
                    data_get_2 = get_data.data
                    message = "Price Info."
                    status = 1
                else:
                    message = "format_id is incorrected."
            else:
                message = "format_id is required."
        else:
            message = "format_id is required."
        return Response({"status":status,"message":message,"data":data_get_2}, status=200)
    

class get_shipping_charge_api(APIView):

    def post(self, request):
        data_get_2 = ""
        status = 0
        message = ""
        if 'country_id' in request.data:
            id = request.data['country_id']
            if id:
                if AwManageShipping.objects.filter(Country__id=id).exists():
                    data = get_object_or_404(AwManageShipping, Country__id=id)
                    get_data = AwManageShippingSerializers(data)
                    data_get_2 = get_data.data
                    message = "Price Info."
                    status = 1
                else:
                    message = "country_id is incorrected."
            else:
                message = "country_id is required."
        else:
            message = "country_id is required."
        return Response({"status":status,"message":message,"data":data_get_2}, status=200)



class get_user_address_list_api(APIView):

    def post(self, request):
        data_get_2 = ""
        status = 0
        message = ""
        if 'user_id' in request.data:
            id = request.data['user_id']
            if id:
                if AwAddressBook.objects.filter(User__id=id).exists():
                    data = get_object_or_404(AwAddressBook, User__id=id)
                    get_data = AwAddressBookSerializare(data)
                    data_get_2 = get_data.data
                    message = "User Address List."
                    status = 1
                else:
                    message = "user_id is incorrected."
            else:
                message = "user_id is required."
        else:
            message = "user_id is required."
        return Response({"status": status, "message": message, "data": data_get_2}, status=200)

class CheckOutViewApi(APIView):

    def post(self, request):
        status = 0
        message = ""
        ordeer_id = ""
        if 'user_id' in request.data:
            user_id = request.data['user_id']
            set_coupon_code = request.data['set_coupon_code']
            set_coupon_type = request.data['set_coupon_type']
            set_coupon_count = request.data['set_coupon_count']
            set_product_amount = request.data['set_product_amount']
            set_order_gst = request.data['set_order_gst']
            order_type = request.data["order_type"]
            payment_type = ""
            quent = 0
            Amount = 0.00
            if User.objects.filter(id=user_id).exists():
                get_user_ins = get_object_or_404(User,id=user_id)
                if AwAddToCard.objects.filter(User=get_user_ins).exists():
                    order_data = AwAddToCard.objects.filter(User=get_user_ins)
                    quent = len(order_data)
                    for item in order_data:
                        if item.Order_Type == "Cellar":
                            if item.Type == 'Bond':
                                if item.Case_Formate.Bond_Descount_Cost > 0:
                                    Amount = Amount + (item.Case_Formate.Bond_Descount_Cost * item.Quentity)
                                else:
                                    Amount = Amount + (item.Case_Formate.Bond_Cost * item.Quentity)
                            if item.Type == 'Retail':
                                if item.Case_Formate.Descount_Cost > 0:
                                    Amount = Amount + (item.Case_Formate.Descount_Cost * item.Quentity)
                                else:
                                    Amount = Amount + (item.Case_Formate.Retail_Cost * item.Quentity)
                        elif item.Order_Type == "Delivered":
                            # if item.order_item_id.Order_id.Payment_Status:
                            #     Amount  = Amount + 0.0
                            # else:
                            Amount = Amount + (item.Old_Cost * item.Quentity)
                        else:
                            Amount = Amount + (item.Event_Ticket.ticket_price * item.Quentity)
                    add_order = AwOrders(User=get_user_ins, Order_Type=order_type, Quentity=quent,Order_Product_Amount=set_product_amount, Order_Gst_Amount=set_order_gst,order_amount=Amount, Amount=Amount, Payment_Method=payment_type)
                    add_order.save()
                    ordeer_id = add_order.order_id
                    if set_coupon_code:
                        Cupon_Discount_amount = 0.0
                        if set_coupon_type == "P":
                            get_persenteg_amoint = (float(Amount) * float(set_coupon_count)) / 100
                            Cupon_Discount_amount = float(Amount) - float(get_persenteg_amoint)
                        else:
                            get_persenteg_amoint = float(set_coupon_count)
                            Cupon_Discount_amount = float(Amount) - float(set_coupon_count)
                        AwOrders.objects.filter(order_id=add_order.order_id).update(Use_coupon=True,Cupon_Code=set_coupon_code,Cupon_Discount=get_persenteg_amoint,Amount=Cupon_Discount_amount)

                    for item in order_data:
                        if item.Order_Type == "Cellar":
                            set_gst = item.Case_Formate.GST
                            set_duty = item.Case_Formate.Duty
                            if item.Type == 'Bond':
                                if item.Case_Formate.Bond_Descount_Cost > 0:
                                    cost_of_product = item.Case_Formate.Bond_Descount_Cost
                                    total_cost = (item.Case_Formate.Bond_Descount_Cost * item.Quentity)
                                else:
                                    cost_of_product = item.Case_Formate.Bond_Cost
                                    total_cost = (item.Case_Formate.Bond_Cost * item.Quentity)
                            if item.Type == 'Retail':
                                if item.Case_Formate.Descount_Cost > 0:
                                    cost_of_product = item.Case_Formate.Descount_Cost
                                    total_cost = (item.Case_Formate.Descount_Cost * item.Quentity)
                                else:
                                    cost_of_product = item.Case_Formate.Retail_Cost
                                    total_cost = (item.Case_Formate.Retail_Cost * item.Quentity)
                        elif item.Order_Type == "Delivered":
                            cost_of_product = item.Old_Cost
                            total_cost = (item.Old_Cost * item.Quentity)
                            set_gst = item.order_item_id.Gst
                            set_duty = item.order_item_id.Duty
                        else:
                            set_gst = 0
                            set_duty = 0
                            cost_of_product = item.Event_Ticket.ticket_price
                            total_cost = (item.Event_Ticket.ticket_price * item.Quentity)
                        Case_Formate_text_set = None
                        if item.Case_Formate:
                            Case_Formate_text_set = item.Case_Formate.Bottle
                        add_item = AwOrederItem(User=get_user_ins, Gst=set_gst, Duty=set_duty, Order_id=add_order,
                                                Product_Cellar=item.Product_Cellar,
                                                Product_Delivered=item.Product_Delivered,
                                                Event_Ticket=item.Event_Ticket, Year=item.Year, Type=item.Type,
                                                Case_Formate_text=Case_Formate_text_set, Case_Formate=item.Case_Formate,
                                                Cost_of_product=cost_of_product, Quentity=item.Quentity,
                                                Order_Quentity=item.Quentity, Total_cost=total_cost)
                        add_item.save()
                        status = 1
                        message = "Order Plase successfully."
                else:
                    message = "No Item avelabel in your card."
            else:
                message = "user_id is incorrect."
        else:
            message = "user_id is required."
        return Response({"status": status, "message": message,"order_id":ordeer_id}, status=200)




class GetOrderInfoApi(APIView):

    def post(self,request):
        status = 0
        message = ""
        ordeer_id = ""
        get_order = ""
        get_order_product = ""
        if "order_id" in request.data:
            order_id = request.data['order_id']
            if AwOrders.objects.filter(order_id=order_id).filter(Order_Status=False).exists():
                get_order_ins = get_object_or_404(AwOrders, order_id=order_id, Order_Status=False)
                get_order_sri =  AwOrdersSerializers(get_order_ins)
                get_order = get_order_sri.data
                if AwOrederItem.objects.filter(User=get_order_ins.User).filter(Order_id=get_order_ins).exists():
                    get_order_product_ins = AwOrederItem.objects.filter(User=get_order_ins.User).filter(Order_id__order_id=order_id).order_by("-id")
                    get_order_product_sri =  AwOrederItemSerializers(get_order_product_ins, many=True)
                    get_order_product = get_order_product_sri.data
                message = "order info."
                status = 1
            else:
                message = "order_id is incorrect."
        else:
            message = "order_id is required."
        return Response({"status": status, "message": message, "get_order": get_order,"get_order_product":get_order_product}, status=200)



class UdateOrderApi(APIView):

    def post(self,request):
        status = 0
        message = ""
        ordeer_id = ""
        if "order_id" in request.data:
            order_id = request.data['order_id']
            payment_type = request.data["payment_type"]
            address_id = request.data["address_id"]
            get_address_ins = None
            my_address = None
            if AwOrders.objects.filter(order_id =order_id).filter(Order_Status=False).exists():
                get_order_ins = get_object_or_404(AwOrders, order_id=order_id,Order_Status=False)
                if AwOrederItem.objects.filter(User=get_order_ins.User).filter(Order_id=get_order_ins).exists():
                    get_acre_product = AwOrederItem.objects.filter(User=get_order_ins.User).filter(Order_id=get_order_ins)
                if get_order_ins.Order_Type == 'Delivered':
                    payment_type = "Payment Done By Caller"
                    if AwAddressBook.objects.filter(id=addres_id).exists():
                        get_address_ins = get_object_or_404(AwAddressBook, id=addres_id)
                    else:
                        message = "addres_id is incorrect."
                if get_order_ins.Order_Type == 'Delivered':
                    shipping_payment_type = request.data["payment_type"]
                    shipping_charge = request.data["shipping_charge"]
                    shipping_Payment_Status_status = True
                else:
                    shipping_payment_type = ""
                    shipping_charge = 0
                    shipping_Payment_Status_status = False

                AwOrders.objects.filter(order_id=order_id).update(shipping_charge=shipping_charge, order_place=True,
                                                                  Order_Status=True, Payment_Status=True,
                                                                  Payment_Method=payment_type,
                                                                  shipping_Payment_Status=shipping_Payment_Status_status,
                                                                  shipping_Payment_Method=shipping_payment_type,
                                                                  Payment_Date=datetime.now(),
                                                                  Order_address=get_address_ins)
                # ==========================remove product from caller when order is develover===================================
                get_product = AwOrederItem.objects.filter(User=get_order_ins.User).filter(Order_id=get_order_ins)

                if AwOrders.objects.filter(User=get_order_ins.User).filter(Order_Type='Caller').exists():
                    get_old_caller_order = AwOrders.objects.filter(User=get_order_ins.User).filter(Order_Type='Caller')

                    for items in get_product:
                        if AwOrederItem.objects.filter(Order_id__in=get_old_caller_order).filter(
                                Product_Cellar=items.Product_Delivered).exists():
                            get_caller = AwOrederItem.objects.filter(Order_id__in=get_old_caller_order).filter(Product_Cellar=items.Product_Delivered)
                            for item_get in get_caller:
                                quentity = item_get.Quentity - items.Quentity
                                if quentity <= 0:
                                    quentity = 0
                                AwOrederItem.objects.filter(id=item_get.id).update(Quentity=quentity)
                                do_updaye_cellar_order_status(item_get.id)
                # ==========================remive product from caller when order is develover===================================
                if get_order_ins.Order_Type == 'Caller':
                    if AwAddToCard.objects.filter(User=get_order_ins.User).exists():
                        get_add_to_cart_order = AwAddToCard.objects.filter(User=get_order_ins.User)
                        for items in get_add_to_cart_order:
                            product = items.Product_Cellar
                            product_price = items.Case_Formate
                            Quentity = items.Quentity
                            Type = items.Type
                            if AwProductPrice.objects.filter(id=items.Case_Formate.id).exists():
                                get_ins = get_object_or_404(AwProductPrice, id=items.Case_Formate.id)
                                if items.Type == 'Retail':
                                    get_old_que = get_ins.Retail_Stock
                                    new = get_ins.Retail_Stock - items.Quentity
                                    AwProductPrice.objects.filter(id=items.Case_Formate.id).update(Retail_Stock=new)
                                else:
                                    get_old_que = get_ins.Bond_Stock
                                    new = get_ins.Bond_Stock - items.Quentity
                                    AwProductPrice.objects.filter(id=items.Case_Formate.id).update(Bond_Stock=new)

                AwAddToCard.objects.filter(User=get_order_ins.User).delete()
                message = "Your Order has placed Successfully."
                status = 1
            else:
                message = "order_id is incorrect."
        else:
            message = "order_id is required."
        return Response({"status": status, "message": message}, status=200)
