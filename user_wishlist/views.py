from django.shortcuts import render,get_object_or_404
from django.template.defaulttags import register
from admin_manage_products.models import AwProducts
from .models import AwWishList
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from orders.models import AwProductPrice
# Create your views here.





@method_decorator(login_required , name="dispatch")
class WishListVidw(generic.ListView):
    model = AwWishList
    template_name = "web/user/page/wishlist/wish_list.html"
    queryset = None
    paginate_by = 10

    def get_queryset(self, **kwargs):
        get_order_items = None
        if AwWishList.objects.filter(user_info=self.request.user).exists():
            get_order_items = AwWishList.objects.filter(user_info=self.request.user)
        return get_order_items

    def get_context_data(self, *args, **kwargs):
        context = super(WishListVidw, self).get_context_data(*args, **kwargs)
        context['Page_title'] = "Wish List"
        return context




def add_product_in_wishlist(request,product_id,vintage_year):
    status = "0"
    if AwProducts.objects.filter(id=product_id).exists():
        product_ins = get_object_or_404(AwProducts,id=product_id)
        user = request.user
        year = vintage_year
        if AwProductPrice.objects.filter(Product=product_ins).filter(Vintage_Year__Vintages_Year=year).exists():
            vinrage_year_ins = get_object_or_404(AwProductPrice,Product=product_ins,Vintage_Year__Vintages_Year=year)
            if AwWishList.objects.filter(user_info=user).filter(Product=product_ins).filter(Case_Formate=vinrage_year_ins).exists():
                AwWishList.objects.filter(user_info=user).filter(Product=product_ins).filter(
                    Case_Formate=vinrage_year_ins).delete()
                status = "1"
                message = "Product is removed in your wishlist."
            else:
                add_data = AwWishList(user_info=user, Product=product_ins, Case_Formate=vinrage_year_ins)
                add_data.save()
                status = "1"
                message = "Product add in your wishlist successfully."
        else:
            message = "vintage_id is in icorrected."
    else:
        message = "product_id is incorrect."
    return JsonResponse({"status": status, "message": message})





@register.filter(name='check_in_wish_list')
def check_in_wish_list(user_ins,product_ins):
    message = ""
    if AwWishList.objects.filter(user_info=user_ins).filter(Product=product_ins).exists():
        message = "whistist-active"
    return message