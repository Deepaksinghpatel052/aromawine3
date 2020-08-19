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
from django.db.models import Q,Subquery
from admin_manage_country.models import AwCountry
from admin_manage_grape.models import AwGrape
from orders.models import AwOrders,AwOrederItem,AwOrderNote
# Create your views here.


class CellarVidw(generic.ListView):
    model = AwOrederItem
    template_name = "web/user/page/cellar/my_cellar.html"
    queryset = None
    paginate_by = 3

    def get_queryset(self, **kwargs):
        get_order_items = None
        filters = None
        if AwOrders.objects.filter(User=self.request.user).filter(Order_Type='Caller').filter(Order_Status=True).exists():
            get_orders = AwOrders.objects.filter(User=self.request.user).filter(Order_Type='Caller').filter(Order_Status=True)
            filters = Q(Order_id__order_id__in=Subquery(get_orders.values('order_id')))
            if AwOrederItem.objects.filter(filters).exists():
                get_order_items = AwOrederItem.objects.filter(filters)
        return get_order_items
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Page_title'] = "My-Cellar"
        context['short_by'] =  self.kwargs.get("short_by")
        get_order_items = None

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
        return context