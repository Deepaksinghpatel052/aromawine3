from django.shortcuts import render,get_object_or_404
from django.views import generic
from admin_manage_products.models import AwProductPrice,AwProducts,AwProductImage,AwWineType
from django.db.models import Count
from django.template.defaulttags import register
from admin_manage_region.models import AwRegion
from admin_manage_Vintages.models import AwVintages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# class DetailView(generic.DetailView):
#     template_name = "web/product_detail/index.html"
#     queryset = AwProducts.objects.filter(id=1)
#
#     def get_object(self, queryset=None):
#         prodict_id = self.kwargs.get("product_id")
#         return get_object_or_404(AwProducts, Product_id=prodict_id)


@register.filter(name='times')
def times(number):
    return range(1,number)


class DetailView(generic.TemplateView):
    template_name = "web/product_detail/index.html"

    def get_context_data(self, **kwargs):
        prodict_id = self.kwargs.get("product_id")
        product_slug = self.kwargs.get("product_slug")
        vintage_year = self.kwargs.get("vintage_year")
        context = super().get_context_data(**kwargs)
        # ================product ins========
        product_ins = None
        vintage_year_ins = None
        if AwProducts.objects.filter(Product_slug=product_slug).exists():
            product_ins = get_object_or_404(AwProducts,Product_slug=product_slug)
            if AwVintages.objects.filter(Vintages_Year=vintage_year).exists():
                vintage_year_ins = get_object_or_404(AwVintages,Vintages_Year=vintage_year)

        get_produuct_years_one_data =None
        get_product_one_year = None
        get_product_all_years = None
        get_product_image = None
        if AwProductPrice.objects.filter(Product=product_ins).exists():
            get_product_all_years = AwProductPrice.objects.filter(Product=product_ins)
            get_produuct_years_one_data = AwProductPrice.objects.filter(Product=product_ins).filter(Vintage_Year=vintage_year_ins)
            get_product_one_year =  AwProductPrice.objects.filter(Product=product_ins).filter(Vintage_Year=vintage_year_ins).first()
            if AwProductImage.objects.filter(Status=True).filter(Product=product_ins).filter(Image_Type="Product_image").exists():
                get_product_image =AwProductImage.objects.filter(Status=True).filter(Product=product_ins).filter(Image_Type="Product_image")[0:3]
        if AwProducts.objects.filter(Status=True).exists():
            get_trending_wines = AwProducts.objects.filter(Status=True)
        context['trending_wines'] = get_trending_wines
        get_vintage_year = AwProductPrice.objects.filter(Vintage_Year=vintage_year_ins).order_by('-Vintage_Year')
        get_years_product = []
        get_filan_vintage_year = []
        if get_vintage_year:
            i = 0
            for items in get_vintage_year:

                if str(items.Vintage_Year.Vintages_Year) + "_" + str(items.Product.Product_name) not in get_years_product:
                    get_filan_vintage_year.append(items)
                    get_years_product.append(str(items.Vintage_Year.Vintages_Year) + "_" + str(items.Product.Product_name))
        context['get_filan_vintage_year'] = get_filan_vintage_year
        context['get_produuct_years_one_data'] = get_produuct_years_one_data
        context['get_product_one_year'] = get_product_one_year
        context['get_product_all_years'] = get_product_all_years
        context['get_product_image'] = get_product_image
        context['Page_title'] = product_ins.Product_slug
        return context
