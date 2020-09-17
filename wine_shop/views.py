from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.http import JsonResponse
from admin_manage_color.models import AwColor
from django.db.models import Max,Min,Count
from admin_manage_products.models import AwProductPrice,AwProducts,AwProductImage,AwWineType
from admin_manage_appellation.models import AwAppellation
from admin_manage_size.models import AwSize
from admin_manage_producer.models import AwProducers
from admin_manage_classification.models import AwClassification
from admin_manage_Vintages.models import AwVintages
from admin_manage_varietals.models import AwVarietals
from admin_manage_region.models import AwRegion
from django.template.defaulttags import register
from .filters import ProductFilter
from admin_manage_categoryes.models import AwCategory
import operator
from django.db.models import Q
from admin_manage_country.models import AwCountry
from admin_manage_grape.models import AwGrape
from .serializers import AwProductPriceSerializers,GetOneProductSerializersValidate,AwProductImageSerializers,GetAllImageOfOneProductSerializersValidate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .api_pagination import ProductLimitOffsetPagination , PrtoductPageNumberPagination
from rest_framework.authentication import TokenAuthentication,SessionAuthentication,BasicAuthentication
from  wineproject.tokens  import account_activation_token,CsrfExemptSessionAuthentication

# Create your views here.

@register.simple_tag
def get_product_count(instance,type):
    product_count = 0
    if type == 'color':
        product_count = AwProductPrice.objects.filter(Product__Color__Slug=instance).count()
    if type  == 'appellation':
        product_count = AwProductPrice.objects.filter(Product__Appellation__Slug=instance).count()
    if type  == 'size':
        product_count = AwProductPrice.objects.filter(Product__Bottel_Size__Slug=instance).count()
    if type  == 'producer':
        product_count = AwProductPrice.objects.filter(Product__Producer__Slug=instance).count()
    if type  == 'classification':
        product_count = AwProductPrice.objects.filter(Product__Classification__Slug=instance).count()
    if type  == 'vintage':
        product_count = AwProductPrice.objects.filter(Vintage_Year__Slug=instance).count()
    if type  == 'varietals':
        product_count = AwProductPrice.objects.filter(Product__Varietals__Slug=instance).count()
    if type  == 'regions':
        product_count = AwProductPrice.objects.filter(Product__Regions__Slug=instance).count()
    return product_count

def product_list(request):
    item  = request.GET["q"]
    get_data = {}
    if AwProductPrice.objects.filter(Q(Product__Product_name__contains=item)|Q(Product__Product_slug__contains=item)|Q(Product__Product_id__contains=item)).exists():
        data = AwProductPrice.objects.filter(Q(Product__Product_name__contains=item)|Q(Product__Product_slug__contains=item)|Q(Product__Product_id__contains=item)).annotate(replies=Count('Vintage_Year') - 1)[:5]
        get_data_sri = AwProductPriceSerializers(data, many=True)
        get_data=get_data_sri.data
    return JsonResponse(get_data,safe=False)


@register.filter(name='get_product_price_with_gst_include')
def get_product_price_with_gst_include(cost,gst):
    get_gst_cost = (cost*gst)/100
    cost_after_gst = cost+get_gst_cost
    return cost_after_gst



class WineFullView(generic.TemplateView):
    template_name = "web/show/product_full_view.html"

class QuickVuewProduct(generic.DetailView):
    template_name = "web/show/quick_detail_product.html"
    model = AwProductPrice

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_all_bottel_set_of_this_year = None
        if AwProductPrice.objects.filter(Product=context['object'].Product).filter(Vintage_Year=context['object'].Vintage_Year).exists():
            get_all_bottel_set_of_this_year = AwProductPrice.objects.filter(Product=context['object'].Product).filter(Vintage_Year=context['object'].Vintage_Year)
        context['get_all_bottel_set_of_this_year'] = get_all_bottel_set_of_this_year
        return context

class ShowView(generic.ListView):
    model = AwProductPrice
    template_name = "web/show/index.html"
    queryset = None
    paginate_by = 10

    def get_queryset(self,**kwargs):
        get_vintage_year = AwProductPrice.objects.filter(Vintage_Year__isnull=False).order_by('-Vintage_Year').annotate(replies=Count('Vintage_Year') - 1)
        get_years_product = []
        get_filan_vintage_year = []
        if get_vintage_year:
            for items in get_vintage_year:
                if str(items.Vintage_Year.Vintages_Year) + "_" + str(
                        items.Product.Product_name) not in get_years_product:
                    get_filan_vintage_year.append(items.id)
                    get_years_product.append(
                        str(items.Vintage_Year.Vintages_Year) + "_" + str(items.Product.Product_name))
        set_filters= 'Vintage_Year'
        if "short-by" in self.request.GET:
            if self.request.GET['short-by'] == "price":
                set_filters = 'Retail_Cost'
            if self.request.GET['short-by'] == "name":
                set_filters = 'Product__Product_name'
        # get_peoduct =
        # get_data = AwProductPrice.objects.filter(id__in = get_filan_vintage_year).order_by(set_filters).annotate(replies=Count('Vintage_Year') - 1)
        # filter_clauses = [Q("Product__Color__Color_name__in" = ['rose-red','Red'])]
        filters = None
        filters = Q(id__in = get_filan_vintage_year)
        # filters = filters & Q(Product__Color__Slug__in=['rose-red','red'])
        # filters = filters & Q(Product__Bottel_Size__Bottle_Size__in=['500 ML'])
        # ======================================COLOR FLTER START======================
        if 'color' in self.request.GET:
            filters = filters & Q(Product__Color__Slug__in=self.request.GET.getlist('color'))
        # ======================================COLOR FLTER END======================
        # ======================================Price FLTER START======================
        if 'min-price' in self.request.GET:
            filters = filters & Q(Retail_Cost__gte=self.request.GET['min-price'])
        if 'max-price' in self.request.GET:
            filters = filters & Q(Retail_Cost__lte=self.request.GET['max-price'])
            
        # ======================================Price FLTER END======================

        # ======================================appellation FLTER START======================
        if 'appellation' in self.request.GET:
            filters = filters & Q(Product__Appellation__Slug__in=self.request.GET.getlist('appellation'))
        # ======================================appellation FLTER END======================
        
        # ======================================bottel-size FLTER START======================
        if 'bottel-size' in self.request.GET:
            filters = filters & Q(Product__Bottel_Size__Slug__in=self.request.GET.getlist('bottel-size'))
        # ======================================bottel-size FLTER END======================

        # ======================================producers FLTER START======================
        if 'producers' in self.request.GET:
            filters = filters & Q(Product__Producer__Slug__in=self.request.GET.getlist('producers'))
        # ======================================producers FLTER END======================

        # ======================================classification FLTER START======================
        if 'classification' in self.request.GET:
            filters = filters & Q(Product__Classification__Slug__in=self.request.GET.getlist('classification'))
        # ======================================classification FLTER END======================

        # ======================================vintage FLTER START======================
        if 'vintage' in self.request.GET:
            filters = filters & Q(Product__Vintage__Slug__in=self.request.GET.getlist('vintage'))
        # ======================================vintage FLTER END======================

        # ======================================varietal FLTER START======================
        if 'varietal' in self.request.GET:
            filters = filters & Q(Product__Varietals__Slug__in=self.request.GET.getlist('varietal'))
        # ======================================varietal FLTER END======================

        # ======================================region FLTER START======================
        if 'region' in self.request.GET:
            filters = filters & Q(Product__Regions__Slug__in=self.request.GET.getlist('region'))
        # ======================================region FLTER END======================

        # ======================================keyword FLTER START======================
        if 'keyword' in self.request.GET:
            filters = filters & Q(Product__Product_slug__contains=self.request.GET['keyword'])
        # ======================================keyword FLTER END======================
        # ======================================category FLTER START======================
        if 'category' in self.request.GET:
            filters = filters & Q(Product__Category__Category_name=self.request.GET['category'])
        # ======================================category FLTER END======================
        # ======================================country FLTER START======================
        if 'country' in self.request.GET:
            filters = filters & Q(Product__Country__Country_Name=self.request.GET['country'])
        # ======================================country FLTER END======================

        # ======================================PAGE FLTER START======================
        if 'page-type' in self.request.GET and 'page-name' in self.request.GET:
            type = self.request.GET['page-type']
            page_slug = self.request.GET['page-name']
            if type == 'grape':
                filters = filters & Q(Product__Grape__Slug=page_slug)
            if type == 'producer':
                filters = filters & Q(Product__Producer__Slug=page_slug)
            if type == 'region':
                filters = filters & Q(Product__Regions__Slug=page_slug)
            if type == 'country':
                filters = filters & Q(Product__Country__Slug=page_slug)


        # ======================================PAGE FLTER END======================


        get_data = AwProductPrice.objects.filter(filters).order_by(set_filters).annotate(replies=Count('Vintage_Year') - 1)
        print(get_data.query)
        return get_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "Wine-shop"
        context['short_by'] =  self.kwargs.get("short_by")
        # print(context)
        # ======================================================================
        get_all_colors =None
        if AwColor.objects.filter(Status=True).exists():
            get_all_colors = AwColor.objects.filter(Status=True)
        context['get_all_colors'] = get_all_colors
        # =====================================================================
        max_price = AwProductPrice.objects.aggregate(Max('Retail_Cost'))
        min_price = AwProductPrice.objects.aggregate(Min('Retail_Cost'))
        context['max_price'] = max_price["Retail_Cost__max"]
        context['min_price'] = min_price["Retail_Cost__min"]
        # =====================================================================
        get_all_appellation = None
        if AwAppellation.objects.filter(Status=True).exists():
            get_all_appellation = AwAppellation.objects.filter(Status=True)
        context['get_all_appellation'] = get_all_appellation
        # =====================================================================
        get_all_size = None
        if AwSize.objects.filter(Status=True).exists():
            get_all_size = AwSize.objects.filter(Status=True)
        context['get_all_size'] = get_all_size
        # =====================================================================
        get_all_producers = None
        if AwProducers.objects.filter(Status=True).exists():
            get_all_producers = AwProducers.objects.filter(Status=True)
        context['get_all_producers'] = get_all_producers
        # =====================================================================
        get_all_classification = None
        if AwClassification.objects.filter(Status=True).exists():
            get_all_classification = AwClassification.objects.filter(Status=True)
        context['get_all_classification'] = get_all_classification
        # =====================================================================
        get_all_vintages = None
        if AwVintages.objects.filter(Status=True).exists():
            get_all_vintages = AwVintages.objects.filter(Status=True)
        context['get_all_vintages'] = get_all_vintages
        # =====================================================================
        get_all_varietals = None
        if AwVarietals.objects.filter(Status=True).exists():
            get_all_varietals = AwVarietals.objects.filter(Status=True)
        context['get_all_varietals'] = get_all_varietals
        # =====================================================================
        get_all_region = None
        if AwRegion.objects.filter(Status=True).exists():
            get_all_region = AwRegion.objects.filter(Status=True)
        context['get_all_region'] = get_all_region
        # =====================================================================
        f = ProductFilter(self.request.GET, queryset=AwProductPrice.objects.all())
        context['filters'] = f
        # =====================================================================
        # ======================================COLOR FLTER START======================
        context['color_set']  = []
        if 'color' in self.request.GET:
            context['color_set'] = self.request.GET.getlist('color')
        # ======================================COLOR FLTER END======================
        # ======================================Price FLTER START======================
        context['min_price_set'] = ""
        context['max_price_set'] = ""
        if 'min-price' in self.request.GET:
            context['min_price_set'] = self.request.GET['min-price']
        if 'max-price' in self.request.GET:
            context['max_price_set'] = self.request.GET['max-price']
            
        # ======================================Price FLTER END======================

        # ======================================COLOR FLTER START======================
        context['appellation_set']  = []
        if 'appellation' in self.request.GET:
            context['appellation_set'] = self.request.GET.getlist('appellation')
        # ======================================COLOR FLTER END======================

        # ======================================bottel-size FLTER START======================
        context['size_set']  = []
        if 'bottel-size' in self.request.GET:
            context['size_set'] = self.request.GET.getlist('bottel-size')
        # ======================================bottel-size FLTER END======================


        # ======================================producers FLTER START======================
        context['producers_set']  = []
        if 'producers' in self.request.GET:
            context['producers_set'] = self.request.GET.getlist('producers')
        # ======================================bottel-size FLTER END======================
        # ======================================classification FLTER START======================
        context['classification_set']  = []
        if 'classification' in self.request.GET:
            context['classification_set']  = self.request.GET.getlist('classification')
        # ======================================classification FLTER END======================

        # ======================================classification FLTER START======================
        context['vintage_set']  = []
        if 'vintage' in self.request.GET:
            context['vintage_set'] =self.request.GET.getlist('vintage')
        # ======================================classification FLTER END======================
        # ======================================varietal FLTER START======================
        context['varietal_set']  = []
        if 'varietal' in self.request.GET:
            context['varietal_set'] = self.request.GET.getlist('varietal')
        # ======================================varietal FLTER END======================

        # ======================================region FLTER START======================
        context['region_set']  = []
        if 'region' in self.request.GET:
            context['region_set'] = self.request.GET.getlist('region')
        # ======================================region FLTER END======================

        # ======================================region FLTER START======================
        context['short_by_set']  = []
        if 'short-by' in self.request.GET:
            context['short_by_set'] = self.request.GET['short-by']
        # ======================================region FLTER END======================
        # ======================================keyword FLTER START======================
        context['keyword_set']  = ""
        if 'keyword' in self.request.GET:
            context['keyword_set'] = self.request.GET['keyword']
        # ======================================keyword FLTER END======================
        # ======================================category FLTER START======================
        context['category_set'] = ""
        context['category_info'] = None
        if 'category' in self.request.GET:
            context['category_set'] = self.request.GET['category']
            context['category_info'] = get_object_or_404(AwCategory,Category_name=self.request.GET['category'] )
        # ======================================category FLTER END======================

        # ======================================country FLTER START======================
        context['country_set'] = ""
        context['country_info'] = ""
        if 'country' in self.request.GET:
            context['country_set'] = self.request.GET['country']
            context['country_info'] = get_object_or_404(AwCountry,Country_Name=self.request.GET['country'] )
        # ======================================country FLTER END======================

        # ============================================SET PAGE FILTER START================================
        page_content = None
        page_title = None
        page_banner_image = None
        Products = None
        context['page_type_set'] = ""
        context['page_slug_set'] = ""
        type = ""
        page_slug = ""
        if 'page-type' in self.request.GET and 'page-name' in self.request.GET:
            type = self.request.GET['page-type']
            page_slug = self.request.GET['page-name']
            context['page_type_set'] = type
            context['page_slug_set'] = page_slug
            # ======================================  FOR grape start ==================================
            if type == 'grape':
                if AwGrape.objects.filter(Slug=page_slug).exists():
                    page_content = get_object_or_404(AwGrape, Slug=page_slug)
                    page_title = page_content.Grape_Name
                    page_banner_image = page_content.Grape_Image
                    if page_content.Grape_banner_Image:
                        page_banner_image = page_content.Grape_banner_Image
                    if AwProductPrice.objects.filter(Product__Grape__Slug=page_slug).exists():
                        Products = AwProductPrice.objects.filter(Product__Grape__Slug=page_slug).annotate(
                            replies=Count('Vintage_Year') - 1)
            # ======================================  FOR grape end ==================================

            # ======================================  FOR AwProducers start ==================================
            if type == 'producer':
                if AwProducers.objects.filter(Slug=page_slug).exists():
                    page_content = get_object_or_404(AwProducers, Slug=page_slug)
                    page_title = page_content.Winnery_Name
                    page_banner_image = page_content.Producer_Image
                    if page_content.Producer_Banner_Image:
                        page_banner_image = page_content.Producer_Banner_Image
                    if AwProductPrice.objects.filter(Product__Producer__Slug=page_slug).exists():
                        Products = AwProductPrice.objects.filter(Product__Producer__Slug=page_slug).annotate(
                            replies=Count('Vintage_Year') - 1)
            # ======================================  FOR grape end ==================================
            # ======================================  FOR AwRegion start ==================================
            if type == 'region':
                if AwRegion.objects.filter(Slug=page_slug).exists():
                    page_content = get_object_or_404(AwRegion, Slug=page_slug)
                    page_title = page_content.Region_Name
                    page_banner_image = page_content.Region_Image
                    if page_content.Region_banner_Image:
                        page_banner_image = page_content.Region_banner_Image
                    if AwProductPrice.objects.filter(Product__Regions__Slug=page_slug).exists():
                        Products = AwProductPrice.objects.filter(Product__Regions__Slug=page_slug).annotate(
                            replies=Count('Vintage_Year') - 1)
            # ======================================  FOR grape end ==================================

            # # ======================================  FOR AwRegion start ==================================
            # if type == 'region':
            #     if AwRegion.objects.filter(Slug=page_slug).exists():
            #         page_content = get_object_or_404(AwRegion, Slug=page_slug)
            #         page_title = page_content.Region_Name
            #         page_banner_image = page_content.Region_Image
            #         if page_content.Region_banner_Image:
            #             page_banner_image = page_content.Region_banner_Image
            #         if AwProductPrice.objects.filter(Product__Regions__Slug=page_slug).exists():
            #             Products = AwProductPrice.objects.filter(Product__Regions__Slug=page_slug).annotate(
            #                 replies=Count('Vintage_Year') - 1)
            # # ======================================  FOR grape end ==================================

            # ======================================  FOR AwCountry start ==================================
            if type == 'country':
                if AwCountry.objects.filter(Slug=page_slug).exists():
                    page_content = get_object_or_404(AwCountry, Slug=page_slug)
                    page_title = page_content.Country_Name
                    page_banner_image = page_content.Country_Image
                    if page_content.Country_Banner_Image:
                        page_banner_image = page_content.Country_Banner_Image
                    if AwProductPrice.objects.filter(Product__Country__Slug=page_slug).exists():
                        Products = AwProductPrice.objects.filter(Product__Country__Slug=page_slug).annotate(
                            replies=Count('Vintage_Year') - 1)
            # ======================================  FOR country end ==================================

        context['page_content'] = page_content
        context['Page_title'] = page_title
        context['page_banner_image'] = page_banner_image
        context['Products'] = Products
        context['type'] = type
        # ============================================SET PAGE FILTER END ================================

        return context



# API START================

class ApiAllImageOfOneProduct(APIView):

    def post(self, request):
        product_image = {}
        serializer = GetAllImageOfOneProductSerializersValidate(data=request.data)
        serializer.is_valid(raise_exception=True)
        get_product_img_sri = AwProductImageSerializers(serializer.validated_data,many=True , context={"request": request})
        product_image = get_product_img_sri.data
        return Response({"product": product_image}, status=200)

class ApiOneWineById(APIView):

    def post(self, request):
        product = {}

        serializer = GetOneProductSerializersValidate(data=request.data)
        serializer.is_valid(raise_exception=True)

        product_seri = AwProductPriceSerializers(serializer.validated_data, context={"request": request})
        product = product_seri.data
        return Response({"product": product}, status=200)


class ApiWineByCategory(generics.ListCreateAPIView):
    serializer_class = AwProductPriceSerializers
    pagination_class = PrtoductPageNumberPagination


    def get_queryset(self, *args, **kwargs):
        product_data = {}
        get_vintage_year = AwProductPrice.objects.filter(Vintage_Year__isnull=False).order_by('-Vintage_Year').annotate(
            replies=Count('Vintage_Year') - 1)
        get_years_product = []
        get_filan_vintage_year = []
        if get_vintage_year:
            for items in get_vintage_year:
                if str(items.Vintage_Year.Vintages_Year) + "_" + str(
                        items.Product.Product_name) not in get_years_product:
                    get_filan_vintage_year.append(items.id)
                    get_years_product.append(
                        str(items.Vintage_Year.Vintages_Year) + "_" + str(items.Product.Product_name))

        filters = None
        filters = Q(id__in=get_filan_vintage_year)

        set_filters = 'Vintage_Year'
        if self.kwargs.get("short_by") == "price":
            set_filters = 'Retail_Cost'
        if self.kwargs.get("short_by") == "name":
            set_filters = 'Product__Product_name'
        filert_by_categort = "All"
        if 'category' in self.request.GET:
            filters = filters & Q(Product__Category__Category_name__in=self.request.GET.getlist('category'))
        if AwProductPrice.objects.filter(filters).annotate(replies=Count('Vintage_Year') - 1).exists():
            product_ins_list = AwProductPrice.objects.filter(filters).annotate(replies=Count('Vintage_Year') - 1)
            total = len(product_ins_list)
            product_ins_list = AwProductPrice.objects.filter(filters).annotate(replies=Count('Vintage_Year') - 1)
        return product_ins_list


# API END================

