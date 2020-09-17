from admin_manage_products.models import AwProductPrice
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from admin_manage_products.models import AwProductImage



class GetAllImageOfOneProductSerializersValidate(serializers.Serializer):
    product_id = serializers.CharField()

    def validate(self, data):
        product_id = data.get("product_id", "")
        product_image = {}
        if product_id:
            if AwProductImage.objects.filter(Product__id=product_id).exists():
                # location_data = get_object_or_404(DfBusinessLocation, id=location_id)
                product_image = AwProductImage.objects.filter(Product__id=product_id)
            else:
                mes = "id is incorrect."
                raise exceptions.ValidationError(mes)
        else:
            mes = "Must provide id."
            raise exceptions.ValidationError(mes)
        return product_image


class GetOneProductSerializersValidate(serializers.Serializer):
    id = serializers.CharField()

    def validate(self, data):
        id = data.get("id", "")
        product_data = {}
        if id:
            if AwProductPrice.objects.filter(id=id).exists():
                # location_data = get_object_or_404(DfBusinessLocation, id=location_id)
                product_data = get_object_or_404(AwProductPrice, id=id)
            else:
                mes = "id is incorrect."
                raise exceptions.ValidationError(mes)
        else:
            mes = "Must provide id."
            raise exceptions.ValidationError(mes)
        return product_data


class AwProductPriceSerializers(serializers.ModelSerializer):
	class Meta:
		model = AwProductPrice
		fields = ['id', 'Product', 'Vintage_Year', 'Bottle', 'Retail_Cost', 'Retail_Stock']
		depth = 2



class AwProductImageSerializers(serializers.ModelSerializer):

	class Meta:
		model = AwProductImage
		fields = ['id', 'Product', 'Image_Type', 'Image', 'Status']

class AwProductPriceSerializers(serializers.ModelSerializer):
	class Meta:
		model = AwProductPrice
		fields = ['id', 'Product', 'Vintage_Year', 'Bottle', 'Retail_Cost', 'Retail_Stock','Descount_Cost','Duty','GST','Bond_Cost','Bond_Stock','Other_info']
		depth = 2