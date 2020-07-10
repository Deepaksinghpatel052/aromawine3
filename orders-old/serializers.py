
from rest_framework import serializers
from admin_manage_products.models import AwProductPrice,AwProducts,AwProductImage
from orders.models import AwAddToCard


class ProductPriceSeriSerializer(serializers.ModelSerializer):
    class Meta:
        model =  AwProductPrice
        fields = ('id', 'Product','Vintage_Year','Bottle', 'Retail_Cost','Retail_Stock', 'Descount_Cost' ,'Duty','GST','Bond_Cost','Bond_Stock','Bond_Descount_Cost','Other_info','Created_by','Created_date','Updated_by','Updated_date')



class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    parent_id = serializers.PrimaryKeyRelatedField(queryset=AwProducts.objects.all(), source='AwAddToCard.Product.id')

    class Meta:
        model = AwProductImage
        fields = ('id', 'Image_Type', 'Image', 'Product','parent_id')

    def create(self, validated_data):
        subject = AwProductImage.objects.create(Product=validated_data['AwAddToCard']['Product']['id'], Image_Type=validated_data['Type'])
        return child


class AwAddToCardSerializer(serializers.ModelSerializer):

    AwProductImage_Product = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model =  AwAddToCard
        fields = ('id','User','Product','Year','Type','Case_Formate','Quentity','Date','AwProductImage_Product')
        depth = 3