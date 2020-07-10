from django.shortcuts import render, HttpResponse,get_object_or_404
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
from addressbook_user.forms import AwAddressBookForm
from addressbook_user.models import AwAddressBook
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
        context['address_form'] = AwAddressBookForm
        my_address = None
        if AwAddressBook.objects.filter(User=self.request.user).exists():
            my_address = AwAddressBook.objects.filter(User=self.request.user)
        context['my_address'] = my_address
        return context


class OrederVidw(generic.TemplateView):
    template_name = 'web/user/page/orders/order_list.html'


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