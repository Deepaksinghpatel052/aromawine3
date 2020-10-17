from django.shortcuts import render,HttpResponseRedirect, HttpResponse,get_object_or_404,redirect
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
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
from admin_manage_categoryes.models import AwCategory
import operator
from django.db.models import Sum
from django.db.models import Q,Subquery
from admin_manage_country.models import AwCountry
from admin_manage_grape.models import AwGrape
from orders.models import AwOrders,AwOrederItem,AwOrderNote
# Create your views here.


class CellarVidw(generic.ListView):
    model = AwOrederItem
    template_name = "web/user/page/cellar/my_cellar.html"
    queryset = None
    # paginate_by = 3

    def get_queryset(self, **kwargs):
        get_order_items = None
        filters = None
        set_filters = 'Vintage_Year'
        if "short-by" in self.request.GET:
            if self.request.GET['short-by'] == "price":
                set_filters = 'Retail_Cost'
            if self.request.GET['short-by'] == "name":
                set_filters = 'Product__Product_name'
        # get_peoduct =
        # get_data = AwProductPrice.objects.filter(id__in = get_filan_vintage_year).order_by(set_filters).annotate(replies=Count('Vintage_Year') - 1)
        # filter_clauses = [Q("Product__Color__Color_name__in" = ['rose-red','Red'])]
        filters = None
        get_years_product = []
        get_filan_vintage_year = []
        get_vintage_year = AwProductPrice.objects.filter(Vintage_Year__isnull=False).order_by('-Vintage_Year').annotate(
            replies=Count('Vintage_Year') - 1)
        if get_vintage_year:
            for items in get_vintage_year:
                if str(items.Vintage_Year.Vintages_Year) + "_" + str(
                        items.Product.Product_name) not in get_years_product:
                    get_filan_vintage_year.append(items.id)
                    get_years_product.append(
                        str(items.Vintage_Year.Vintages_Year) + "_" + str(items.Product.Product_name))

        filters = None
        filters = Q(Case_Formate__id__in=get_filan_vintage_year)
        # filters = filters & Q(Product__Color__Slug__in=['rose-red','red'])
        # filters = filters & Q(Product__Bottel_Size__Bottle_Size__in=['500 ML'])
        # ======================================COLOR FLTER START======================
        if 'color' in self.request.GET:
            filters = filters & Q(Product_Cellar__Color__Slug__in=self.request.GET.getlist('color'))
        # ======================================COLOR FLTER END======================
        # ======================================Price FLTER START======================
        if 'min-price' in self.request.GET:
            filters = filters & Q(Case_Formate__Retail_Cost__gte=self.request.GET['min-price'])
        if 'max-price' in self.request.GET:
            filters = filters & Q(Case_Formate__Retail_Cost__lte=self.request.GET['max-price'])

        # ======================================Price FLTER END======================

        # ======================================appellation FLTER START======================
        if 'appellation' in self.request.GET:
            filters = filters & Q(Product_Cellar__Appellation__Slug__in=self.request.GET.getlist('appellation'))
        # ======================================appellation FLTER END======================

        # ======================================bottel-size FLTER START======================
        if 'bottel-size' in self.request.GET:
            filters = filters & Q(Product_Cellar__Bottel_Size__Slug__in=self.request.GET.getlist('bottel-size'))
        # ======================================bottel-size FLTER END======================

        # ======================================producers FLTER START======================
        if 'producers' in self.request.GET:
            filters = filters & Q(Product_Cellar__Producer__Slug__in=self.request.GET.getlist('producers'))
        # ======================================producers FLTER END======================

        # ======================================classification FLTER START======================
        if 'classification' in self.request.GET:
            filters = filters & Q(Product_Cellar__Classification__Slug__in=self.request.GET.getlist('classification'))
        # ======================================classification FLTER END======================

        # ======================================vintage FLTER START======================
        if 'vintage' in self.request.GET:
            filters = filters & Q(Product_Cellar__Vintage__Slug__in=self.request.GET.getlist('vintage'))
        # ======================================vintage FLTER END======================

        # ======================================varietal FLTER START======================
        if 'varietal' in self.request.GET:
            filters = filters & Q(Product_Cellar__Varietals__Slug__in=self.request.GET.getlist('varietal'))
        # ======================================varietal FLTER END======================

        # ======================================region FLTER START======================
        if 'region' in self.request.GET:
            filters = filters & Q(Product_Cellar__Regions__Slug__in=self.request.GET.getlist('region'))
        # ======================================region FLTER END======================

        # ======================================keyword FLTER START======================
        if 'keyword' in self.request.GET:
            filters = filters & Q(Product_Cellar__Product_slug__contains=self.request.GET['keyword'])
        # ======================================keyword FLTER END======================
        # ======================================category FLTER START======================
        if 'category' in self.request.GET:
            filters = filters & Q(Product_Cellar__Category__Category_name=self.request.GET['category'])
        # ======================================category FLTER END======================
        # ======================================country FLTER START======================
        if 'country' in self.request.GET:
            filters = filters & Q(Product_Cellar__Country__Country_Name=self.request.GET['country'])
        # ======================================country FLTER END======================

        # ======================================PAGE FLTER START======================
        if 'page-type' in self.request.GET and 'page-name' in self.request.GET:
            type = self.request.GET['page-type']
            page_slug = self.request.GET['page-name']
            if type == 'grape':
                filters = filters & Q(Product_Cellar__Grape__Slug=page_slug)
            if type == 'producer':
                filters = filters & Q(Product_Cellar__Producer__Slug=page_slug)
            if type == 'region':
                filters = filters & Q(Product_Cellar__Regions__Slug=page_slug)
            if type == 'country':
                filters = filters & Q(Product_Cellar__Country__Slug=page_slug)

        # ======================================PAGE FLTER END======================

        if AwOrders.objects.filter(User=self.request.user).filter(Order_Type='Caller').filter(Order_Status=True).exists():
            get_orders = AwOrders.objects.filter(User=self.request.user).filter(Order_Type='Caller').filter(Order_Status=True)
            filters = filters & Q(Order_id__order_id__in=Subquery(get_orders.values('order_id')))
            if AwOrederItem.objects.filter(filters).exists():
                get_order_items = AwOrederItem.objects.filter(filters)
        return get_order_items
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "My-Cellar"
        context['short_by'] =  self.kwargs.get("short_by")
        get_order_items = None
        # ====================================
        total_unique_wine =  0
        total_unite =  0
        total_cost_of_caller =  0
        if AwOrederItem.objects.filter(Order_id__Order_Type='Caller').filter(Quentity__gt=0).filter(Order_id__Payment_Status=True).exists():
            product_quantity_info = (AwOrederItem.objects.values('Product_Cellar', 'Year','Quentity').filter(Quentity__gt=0).filter(User=self.request.user).filter(Order_id__Order_Type='Caller').filter(Order_id__Payment_Status=True).annotate(
            total=Count('id')))
            total_unique_wine = len(product_quantity_info)
            for item in product_quantity_info:
                total_unite = total_unite + item['Quentity']

            total_omount_of_caller_products = AwOrederItem.objects.filter(Quentity__gt=0).filter(User=self.request.user).filter(Order_id__Order_Type='Caller').filter(Order_id__Payment_Status=True)
          
            for caller_amounrt in total_omount_of_caller_products:
                total_cost_of_caller = total_cost_of_caller + (caller_amounrt.Quentity * caller_amounrt.Cost_of_product)

        context['total_unique_wine'] = total_unique_wine
        context['total_unite'] = total_unite
        context['total_cost_of_caller'] = total_cost_of_caller
        # ====================================

        context['get_order_items'] = get_order_items
        # ======================================================================
        get_all_colors = None
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


        # =================================URL DATA START ===========================
        # ======================================COLOR FLTER START======================
        context['color_set'] = []
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
        context['appellation_set'] = []
        if 'appellation' in self.request.GET:
            context['appellation_set'] = self.request.GET.getlist('appellation')
        # ======================================COLOR FLTER END======================

        # ======================================bottel-size FLTER START======================
        context['size_set'] = []
        if 'bottel-size' in self.request.GET:
            context['size_set'] = self.request.GET.getlist('bottel-size')
        # ======================================bottel-size FLTER END======================

        # ======================================producers FLTER START======================
        context['producers_set'] = []
        if 'producers' in self.request.GET:
            context['producers_set'] = self.request.GET.getlist('producers')
        # ======================================bottel-size FLTER END======================
        # ======================================classification FLTER START======================
        context['classification_set'] = []
        if 'classification' in self.request.GET:
            context['classification_set'] = self.request.GET.getlist('classification')
        # ======================================classification FLTER END======================

        # ======================================classification FLTER START======================
        context['vintage_set'] = []
        if 'vintage' in self.request.GET:
            context['vintage_set'] = self.request.GET.getlist('vintage')
        # ======================================classification FLTER END======================
        # ======================================varietal FLTER START======================
        context['varietal_set'] = []
        if 'varietal' in self.request.GET:
            context['varietal_set'] = self.request.GET.getlist('varietal')
        # ======================================varietal FLTER END======================

        # ======================================region FLTER START======================
        context['region_set'] = []
        if 'region' in self.request.GET:
            context['region_set'] = self.request.GET.getlist('region')
        # ======================================region FLTER END======================

        # ======================================region FLTER START======================
        context['short_by_set'] = []
        if 'short-by' in self.request.GET:
            context['short_by_set'] = self.request.GET['short-by']
        # ======================================region FLTER END======================
        # ======================================keyword FLTER START======================
        context['keyword_set'] = ""
        if 'keyword' in self.request.GET:
            context['keyword_set'] = self.request.GET['keyword']
        # ======================================keyword FLTER END======================
        # ======================================category FLTER START======================
        context['category_set'] = ""
        context['category_info'] = None
        if 'category' in self.request.GET:
            context['category_set'] = self.request.GET['category']
            context['category_info'] = get_object_or_404(AwCategory, Category_name=self.request.GET['category'])
        # ======================================category FLTER END======================

        # ======================================country FLTER START======================
        context['country_set'] = ""
        context['country_info'] = ""
        if 'country' in self.request.GET:
            context['country_set'] = self.request.GET['country']
            context['country_info'] = get_object_or_404(AwCountry, Country_Name=self.request.GET['country'])
        # ======================================country FLTER END======================
        
        # =================================URL DATA END ===========================





        return context