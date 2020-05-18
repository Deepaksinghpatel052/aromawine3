from django.shortcuts import render
from django.views import generic
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
# Create your views here.

def product_list(request):
    f = ProductFilter(request.GET, queryset=AwProductPrice.objects.all())
    return render(request, 'admin_manage_products/awproductprice_filter.html', {'filter': f})


@register.filter(name='get_product_price_with_gst_include')
def get_product_price_with_gst_include(cost,gst):
    get_gst_cost = (cost*gst)/100
    cost_after_gst = cost+get_gst_cost
    return cost_after_gst

class QuickVuewProduct(generic.DetailView):
    template_name = "web/show/quick_detail_product.html"
    model = AwProductPrice

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("====================dsp=======")
        print(context['object'])
        get_all_bottel_set_of_this_year = None
        if AwProductPrice.objects.filter(Product=context['object'].Product).filter(Vintage_Year=context['object'].Vintage_Year).exists():
            get_all_bottel_set_of_this_year = AwProductPrice.objects.filter(Product=context['object'].Product).filter(Vintage_Year=context['object'].Vintage_Year)
        context['get_all_bottel_set_of_this_year'] = get_all_bottel_set_of_this_year
        return context

class ShowView(generic.ListView):
    model = AwProductPrice
    template_name = "web/show/index.html"
    queryset = None
    paginate_by = 5

    def get_queryset(self,**kwargs):
        print("-----------------------")

        print("-----------------------")
        get_vintage_year = AwProductPrice.objects.all().order_by('-Vintage_Year').annotate(replies=Count('Vintage_Year') - 1)
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
        if self.kwargs.get("short_by") == "price":
            set_filters = 'Retail_Cost'
        if self.kwargs.get("short_by") == "name":
            set_filters = 'Product__Product_name'
        # get_peoduct =
        # get_data = ProductFilter(self.request.GET, queryset=get_peoduct)
        return AwProductPrice.objects.filter(id__in = get_filan_vintage_year).order_by(set_filters).annotate(replies=Count('Vintage_Year') - 1)

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

        return context


