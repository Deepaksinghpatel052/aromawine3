from django.shortcuts import render,get_object_or_404
from django.views import generic
from admin_manage_products.models import AwProductPrice,AwProducts,AwProductImage,AwWineType,AwProductImageFullView,AwProductReviews
from django.db.models import Count
from django.template.defaulttags import register
from admin_manage_region.models import AwRegion
from admin_manage_Vintages.models import AwVintages
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import  exceptions
from django.db.models import Q
from wine_palate.models import  AwUserPalateWine
from .serializear  import AwProductsSerilizear,AwProductPriceSerilizear,AwProductImageSerilizear,GetOneProductValidationSerializers
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




class DetailViewApi(APIView):


    def get(self,request,**kwargs):
        prodict_id = self.kwargs.get("product_id")
        product_slug = self.kwargs.get("product_slug")
        vintage_year = self.kwargs.get("vintage_year")
        # get_data = {"product_id":prodict_id,"product_slug":product_slug,"vintage_year":vintage_year}
        # serializer = GetOneProductValidationSerializers(data=get_data)
        # serializer.is_valid(raise_exception=True)
        product_ins = None
        vintage_year_ins = None
        if AwProducts.objects.filter(Product_slug=product_slug).exists():
            product_ins = get_object_or_404(AwProducts,Product_slug=product_slug)
            if AwVintages.objects.filter(Vintages_Year=vintage_year).exists():
                vintage_year_ins = get_object_or_404(AwVintages,Vintages_Year=vintage_year)
            else:
                mes = "Your vintage_year is incorrect"
                raise exceptions.ValidationError(mes)
        else:
            mes = "Your product_slug is incorrect"
            raise exceptions.ValidationError(mes)
        get_produuct_years_one_data ={}
        get_product_one_year = {}
        get_product_all_years = {}
        get_product_image = {}
        if AwProductPrice.objects.filter(Product=product_ins).exists():
            get_product_all_years = AwProductPrice.objects.filter(Product=product_ins)
            get_produuct_years_one_data = AwProductPrice.objects.filter(Product=product_ins).filter(Vintage_Year=vintage_year_ins)
            get_product_one_year =  AwProductPrice.objects.filter(Product=product_ins).filter(Vintage_Year=vintage_year_ins).first()
            if AwProductImage.objects.filter(Status=True).filter(Product=product_ins).filter(Image_Type="Product_image").exists():
                get_product_image =AwProductImage.objects.filter(Status=True).filter(Product=product_ins).filter(Image_Type="Product_image")[0:3]

        data = {}
        data["prodict_id"] = prodict_id
        data["product_slug"] = product_slug
        data["vintage_year"] = vintage_year

        get_product_one_year_sri = AwProductPriceSerilizear(get_product_one_year)
        data["get_product_one_year"] = get_product_one_year_sri.data


        get_produuct_years_one_data_sri = AwProductPriceSerilizear(get_produuct_years_one_data,many=True)
        data["get_produuct_years_one_data"] = get_produuct_years_one_data_sri.data

        get_product_all_years_sri = AwProductPriceSerilizear(get_product_all_years, many=True)
        data["get_product_all_years"] = get_product_all_years_sri.data

        get_product_image_sri = AwProductImageSerilizear(get_product_image, many=True,context={"request": request})
        data["get_product_image"] = get_product_image_sri.data

        return Response({"message": "get data","data":data}, status=200)






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
        get_filan_vintage_year_id = []
        if get_vintage_year:
            i = 0
            for items in get_vintage_year:

                if str(items.Vintage_Year.Vintages_Year) + "_" + str(items.Product.Product_name) not in get_years_product:
                    get_filan_vintage_year.append(items)
                    get_filan_vintage_year_id.append(items.id)
                    get_years_product.append(str(items.Vintage_Year.Vintages_Year) + "_" + str(items.Product.Product_name))

        get_product_review = None
        if get_product_one_year.Product.LWineCode:
            l_wine_code =  str(get_product_one_year.Product.LWineCode)+str(get_product_one_year.Vintage_Year.Vintages_Year)
            if AwProductReviews.objects.filter(LWineCode=l_wine_code).exists():
                get_product_review = AwProductReviews.objects.filter(LWineCode=l_wine_code)

        context['get_filan_vintage_year'] = get_filan_vintage_year
        context['get_produuct_years_one_data'] = get_produuct_years_one_data
        context['get_product_one_year'] = get_product_one_year
        context['get_product_all_years'] = get_product_all_years
        context['get_product_image'] = get_product_image
        context['Page_title'] = product_ins.Product_slug
        context['get_product_review'] = get_product_review






        get_all_palate_info_of_user = None
        get_data_according_to_palate_profile = None
        get_list_of_my_palate = []
        if self.request.user.is_authenticated:
            if AwUserPalateWine.objects.filter(User=self.request.user).exists():
                get_all_palate_info_of_user = AwUserPalateWine.objects.filter(User=self.request.user).order_by("-id")
            context['get_all_palate_info_of_user'] = get_all_palate_info_of_user
            if get_all_palate_info_of_user:
                for item in get_all_palate_info_of_user:
                    get_list_of_my_palate.append(item.Type)

                filters = None
                # filters = Q(id__in=get_filan_vintage_year_id)
                filters =  Q(Product__Category__Category_name__in=get_list_of_my_palate)

                if AwProductPrice.objects.filter(filters).exists():
                    get_data_according_to_palate_profile = AwProductPrice.objects.filter(filters).annotate(replies=Count('Vintage_Year') - 1)
        context['get_data_according_to_palate_profile'] = get_data_according_to_palate_profile
        image_of_full_view = None
        if AwProductImageFullView.objects.filter(Product=product_ins).exists():
            image_of_full_view = AwProductImageFullView.objects.filter(Product=product_ins)
        context['image_of_full_view'] = image_of_full_view
        return context




