from admin_manage_products.models import AwProductPrice
from rest_framework import serializers

class AwProductPriceSerializers(serializers.ModelSerializer):
	class Meta:
		model = AwProductPrice
		fields = ['id', 'Product', 'Vintage_Year', 'Bottle', 'Retail_Cost', 'Retail_Stock']
		depth = 2