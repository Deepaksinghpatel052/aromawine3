from django.shortcuts import render,HttpResponseRedirect, HttpResponse,get_object_or_404,redirect
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from admin_manage_products.models import AwProductPrice,AwProducts
from orders.serializers import ProductPriceSeriSerializer,AwAddToCardSerializer
from orders.models import AwAddToCard
from admin_manage_setting.models import AwManageShipping
from django.template.defaulttags import register
from django.template.loader import render_to_string
from profile_user.models import AwUserInfo
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from addressbook_user.forms import AwAddressBookFormUser,AwAddressBookForm
from addressbook_user.models import AwAddressBook
from .models import AwOrders,AwOrederItem,AwOrderNote
from django.urls import reverse
from manage_event.models import AwEvent
from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from wineproject import settings
from admin_manage_cupon_code.models import AwCuponCode
from datetime import datetime
from datetime import date
from django.db.models import Q
# Create your views here.

@csrf_exempt
def get_country_id(request):
    address_id = request.POST['address_id']
    address_book_ins = get_object_or_404(AwAddressBook,id=address_id)
    return JsonResponse({"country_id":address_book_ins.Country.id})

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
        messages.info(request, 'Product remove from card successfully')
    else:
        messages.error(request, "Product is not remove.")
    return redirect(settings.BASE_URL + "user/orders/my-cart")

# @method_decorator(login_required , name="dispatch")
class MyCardView(generic.TemplateView):
    template_name = "web/user/page/orders/my_card.html"

    def get_context_data(self, *args, **kwargs):
        context = super(MyCardView, self).get_context_data(*args, **kwargs)
        context['Page_title'] = "My-Card"
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
            add_item = AwOrederItem(User=request.user, Gst=set_gst,Duty=set_duty, Order_id=add_order, Product_Cellar=item.Product_Cellar,Product_Delivered=item.Product_Delivered,Event_Ticket=item.Event_Ticket, Year=item.Year,Type=item.Type, Case_Formate_text=Case_Formate_text_set,Case_Formate=item.Case_Formate,Cost_of_product=cost_of_product, Quentity=item.Quentity, Total_cost=total_cost)
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
        # ==========================remive product from caller when order is develover===================================
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
            if AwOrederItem.objects.filter(Product_Cellar__Product_id=product_id).filter(Order_id__id=order_id).filter(Year=Year).exists():
                product_order_item_ins_all_data= get_object_or_404(AwOrederItem, Product_Cellar__Product_id=product_id, Order_id__id=order_id,Year=Year)
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
                    message = "You can add only ont type "+set_item_type+" ("+str(get_filst_item_ins.Order_Type)+")."
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