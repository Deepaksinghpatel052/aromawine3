from django.shortcuts import render,get_object_or_404
from django.views import generic
from admin_manage_products.models import AwProductPrice,AwProducts,AwProductImage,AwWineType
from django.db.models import Count
from django.template.defaulttags import register
from .models import AwAboutAromaWines
from admin_manage_region.models import AwRegion
from admin_manage_banners.models import AwBanners
# Create your views here.

@register.filter(name='get_product_image_one')
def get_product_image_one(product_ins):
    get_image = "/static/web/assets/image/shop/1.jpg"
    if product_ins:
        if AwProductImage.objects.filter(Product=product_ins).exists():
            get_product_image = AwProductImage.objects.filter(Product=product_ins).filter(Image_Type="Product_image")
            if get_product_image:
                get_image = get_product_image[0].Image.url
    return get_image

@register.filter(name='get_product_vintage_yera_one')
def get_product_vintage_yera_one(product_ins):
    vintage_year = ""
    if product_ins:
        if AwProductPrice.objects.filter(Product=product_ins).exists():
            get_product_vintage_ins = AwProductPrice.objects.filter(Product=product_ins).order_by("?").first()
            vintage_year = get_product_vintage_ins.Vintage_Year.Vintages_Year
    return vintage_year

class HomeView(generic.TemplateView):
    template_name = "web/home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Home"
        get_trending_wines = None
        if AwProducts.objects.filter(Status=True).exists():
            get_trending_wines = AwProducts.objects.filter(Status=True)
        context['trending_wines'] = get_trending_wines

        get_all_wines = None
        if AwWineType.objects.filter(Type='Wine').filter(Status=True).exists():
            get_wine_type_ins = get_object_or_404(AwWineType,Type='Wine',Status=True)
            if AwProducts.objects.filter(Status=True).filter(Select_Type=get_wine_type_ins).exists():
                get_all_wines = AwProducts.objects.filter(Status=True).filter(Select_Type=get_wine_type_ins)
        context['get_all_wines'] = get_all_wines

        # ==================== set vintage data start========================

        get_vintage_year = AwProductPrice.objects.all().order_by('-Vintage_Year')
        get_years_product = []
        get_filan_vintage_year = []
        if get_vintage_year:
            i=0
            for items in get_vintage_year:
               if i < 5:
                   if str(items.Vintage_Year.Vintages_Year)+"_"+str(items.Product.Product_name) not in get_years_product:
                       get_filan_vintage_year.append(items)
                       get_years_product.append(str(items.Vintage_Year.Vintages_Year)+"_"+str(items.Product.Product_name))
                       i =i+1
        context['get_filan_vintage_year'] = get_filan_vintage_year

        get_region = None
        if AwRegion.objects.filter(Status=True).exists():
            get_region = AwRegion.objects.filter(Status=True)

        context['get_region'] = get_region
        # =====================get regions  End=============

        # =====================get slder Image  start=============
        get_slider = None
        if AwBanners.objects.filter(Status=True).filter(Type="Home Banner").exists():
            get_slider = AwBanners.objects.filter(Status=True).filter(Type="Home Banner")

        context['get_slider'] = get_slider
        # =====================get regions  End=============
        # ==================== set vintage data end ========================
        get_about_wine = None
        if AwBanners.objects.filter(Status=True).filter(Type="About Aroma").exists():
            get_about_wine = AwBanners.objects.filter(Status=True).filter(Type="About Aroma").first()
        context['get_about_wine'] = get_about_wine

        # =====================get regions  start=============
        # print(get_vintage_year_ids)
        return context