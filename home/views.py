from django.shortcuts import render,get_object_or_404
from django.views import generic
from admin_manage_products.models import AwProductPrice,AwProducts,AwProductImage,AwWineType
from django.db.models import Count
from django.template.defaulttags import register
from .models import AwAboutAromaWines,AwCmsPaage
from admin_manage_region.models import AwRegion
from admin_manage_banners.models import AwBanners
from admin_manage_categoryes.models import AwCategory
from admin_manage_appellation.models import AwAppellation
from django.template.loader import render_to_string
from django.db.models import Q
from admin_manage_country.models import AwCountry
from admin_manage_producer.models import AwSetTo,AwProducers
from admin_manage_Vintages.models import AwVintages
# Create your views here.


@register.filter(name='get_wine_according_region')
def get_wine_according_region(region):
    get_product = None
    if AwProductPrice.objects.filter(Product__Category__Category_name='Fine Wine').filter(Product__Regions__Region_Name=region).filter(Product__Status=True).filter(Vintage_Year__isnull=False).exists():
        get_product = AwProductPrice.objects.filter(Product__Category__Category_name='Fine Wine').filter(Product__Regions__Region_Name=region).filter(Product__Status=True).filter(Vintage_Year__isnull=False)
    return render_to_string('web/home/regions/get_product_by_region.html',{"get_product":get_product})

@register.filter(name='get_wine_according_category')
def get_wine_according_category(category):
    get_product = None
    if AwProductPrice.objects.filter(Product__Category__Category_name='Aroma of Wine').filter(Product__Category__Category_name=category).filter(Product__Status=True).filter(Vintage_Year__isnull=False).annotate(replies=Count('Vintage_Year') - 1).exists():
        get_product = AwProductPrice.objects.filter(Product__Category__Category_name='Aroma of Wine').filter(Product__Category__Category_name=category).filter(Product__Status=True).filter(Vintage_Year__isnull=False).annotate(replies=Count('Vintage_Year') - 1)
    return render_to_string('web/home/category/get_product.html',{"get_product":get_product})

@register.filter(name='get_wine_according_aroma_selection')
def get_wine_according_aroma_selection(category):
    get_product = None
    if AwProductPrice.objects.filter(Product__Category__Category_name='Aroma Selection').filter(Product__Category__Category_name=category).filter(Product__Status=True).filter(Vintage_Year__isnull=False).annotate(replies=Count('Vintage_Year') - 1).exists():
        get_product = AwProductPrice.objects.filter(Product__Category__Category_name='Aroma Selection').filter(Product__Category__Category_name=category).filter(Product__Status=True).filter(Vintage_Year__isnull=False).annotate(replies=Count('Vintage_Year') - 1)
    return render_to_string('web/home/category/get_product.html',{"get_product":get_product})


@register.filter(name='show_mega_menu')
def show_mega_menu(dummt_data):
    get_category = None
    get_region_for_fine_wine = None
    aromawine_pattenre_country= None
    fine_wine_ins = get_object_or_404(AwSetTo,Title='Fine Wines')
    if AwCategory.objects.filter(Status=True).exists():
        get_category = AwCategory.objects.filter(Status=True).order_by("Category_name")

    if AwRegion.objects.filter(Status=True).filter(Set_To__Title='Fine Wines').exists():
        get_region_for_fine_wine = AwRegion.objects.filter(Status=True).filter(Set_To__Title='Fine Wines').order_by("Region_Name")
    aromawine_pattenre_country = None
    aromawine_pattenre_winnery = None
    aromawine_pattenre_applicant = None
    if AwCountry.objects.filter(Set_To__Title='Aroma Wine partners').exists():
        aromawine_pattenre_country = AwCountry.objects.filter(Set_To__Title='Aroma Wine partners').order_by('Country_Name')
    if AwProducers.objects.filter(Set_To__Title='Aroma Wine partners').exists():
        aromawine_pattenre_winnery = AwProducers.objects.filter(Set_To__Title='Aroma Wine partners').order_by('Winnery_Name')
    if AwAppellation.objects.filter(Set_To__Title='Aroma Wine partners').exists():
        aromawine_pattenre_applicant = AwAppellation.objects.filter(Set_To__Title='Aroma Wine partners').order_by('Appellation_Name')


    en_premier_vintage_year = None
    en_premier_vintage_winnery = None
    en_premier_vintage_wine = None
    if AwVintages.objects.filter(Set_To__Title='En Premier').exists():
        en_premier_vintage_year = AwVintages.objects.filter(Set_To__Title='En Premier').order_by('Vintages_Year')
    if AwProducers.objects.filter(Set_To__Title='En Premier').exists():
        en_premier_vintage_winnery = AwProducers.objects.filter(Set_To__Title='En Premier').order_by('Winnery_Name')
    if AwProducers.objects.filter(Set_To__Title='En Premier').exists():
        en_premier_vintage_winnery = AwProducers.objects.filter(Set_To__Title='En Premier').order_by('Winnery_Name')
    if AwProductPrice.objects.filter(Product__Category__Category_name='En Premier').filter(Product__Status=True).filter(Vintage_Year__isnull=False).annotate(replies=Count('Vintage_Year') - 1).exists():
        en_premier_vintage_wine = AwProductPrice.objects.filter(Product__Category__Category_name='En Premier').filter(Product__Status=True).filter(Vintage_Year__isnull=False).annotate(replies=Count('Vintage_Year') - 1)

    sprit_country = None
    sprit_product = None
    if AwCountry.objects.filter(Set_To__Title='Sprits').exists():
        sprit_country = AwCountry.objects.filter(Set_To__Title='Sprits').order_by('Country_Name')
    if AwProductPrice.objects.filter(Product__Select_Type__Type='Sprits').filter(Product__Status=True).filter(Vintage_Year__isnull=False).annotate(replies=Count('Vintage_Year') - 1).exists():
        sprit_product = AwProductPrice.objects.filter(Product__Select_Type__Type='Sprits').filter(Product__Status=True).filter(Vintage_Year__isnull=False).annotate(replies=Count('Vintage_Year') - 1)
    return render_to_string('web/home/mega_menu.html',{'sprit_product':sprit_product,'sprit_country':sprit_country,'en_premier_vintage_year':en_premier_vintage_year,'en_premier_vintage_winnery':en_premier_vintage_winnery,'en_premier_vintage_wine':en_premier_vintage_wine, "get_category":get_category,'get_region_for_fine_wine':get_region_for_fine_wine,'aromawine_pattenre_country':aromawine_pattenre_country,'aromawine_pattenre_winnery':aromawine_pattenre_winnery,'aromawine_pattenre_applicant':aromawine_pattenre_applicant})



@register.filter(name='get_product_image_one')
def get_product_image_one(product_ins):
    get_image = "/static/web/assets/image/shop/single-1.png "
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
            get_product_vintage_ins = AwProductPrice.objects.filter(Product=product_ins).filter(Vintage_Year__isnull=False).order_by("?").first()
            if get_product_vintage_ins.Vintage_Year:
                vintage_year = get_product_vintage_ins.Vintage_Year.Vintages_Year
    return vintage_year

@register.filter(name='show_footer')
def show_footer(dummy_data):
    catrregory = None
    custom_page = None
    if AwCategory.objects.filter(Status=True).exists():
        catrregory = AwCategory.objects.filter(Status=True).order_by('Category_name')[:9]
    if AwCmsPaage.objects.all().exists():
        custom_page = AwCmsPaage.objects.all().order_by('Title')[:5]
    return render_to_string('web/home/footer_page.html',{'catrregory':catrregory,'custom_page':custom_page})


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

        get_vintage_year = AwProductPrice.objects.filter(Product__Status=True).filter(Product__Category__Category_name='Aroma recommendations').order_by('-Vintage_Year')
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

class CustomPageView(generic.TemplateView):
    template_name = "web/home/page_content.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_slug = self.kwargs.get("title")
        get_page_info = None
        if AwCmsPaage.objects.filter(Slug=page_slug).exists():
            get_page_info = get_object_or_404(AwCmsPaage , Slug=page_slug)
        context['get_page_info'] = get_page_info
        return context



