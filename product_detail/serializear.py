from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework import  exceptions
from admin_manage_products.models import AwProductPrice,AwProducts,AwProductImage,AwWineType,AwProductImageFullView



class GetOneProductValidationSerializers(serializers.Serializer):
    product_id = serializers.CharField(style={"inpupt_type": "number"}, write_only=True)
    product_slug = serializers.CharField(style={"inpupt_type": "number"}, write_only=True)
    vintage_year = serializers.CharField(style={"inpupt_type": "number"}, write_only=True)

    def validate(self, data):
        get_product = None
        product_id = data.get("product_id", "")
        product_slug = data.get("product_slug", "")
        vintage_year = data.get("vintage_year", "")
        if AwProducts.objects.filter(Product_slug=product_id).exists():
            AwProducts_ins = get_object_or_404(AwProducts,Product_id=product_id)
        else:
            mes = "Your product_id is incorrect."
            raise exceptions.ValidationError(mes)
        if AwProducts.objects.filter(Product_slug=product_slug).exists():
            AwProducts_ins = get_object_or_404(AwProducts,Product_slug=product_slug)
            if AwVintages.objects.filter(Vintages_Year=vintage_year).exists():
                vintage_year_ins = get_object_or_404(AwVintages, Vintages_Year=vintage_year)
            else:
                mes = "Your vintage_year is incorrect."
                raise exceptions.ValidationError(mes)
        else:
            mes = "Your product_slug is incorrect."
            raise exceptions.ValidationError(mes)
        return location_id_get



class AwProductsSerilizear(serializers.ModelSerializer):
    class Meta:
        model = AwProducts
        fields = '__all__'
        depth = 2


class AwProductPriceSerilizear(serializers.ModelSerializer):
    class Meta:
        model = AwProductPrice
        fields = '__all__'
        depth = 2

class AwProductImageSerilizear(serializers.ModelSerializer):
    class Meta:
        model = AwProductImage
        fields = '__all__'
        depth = 2