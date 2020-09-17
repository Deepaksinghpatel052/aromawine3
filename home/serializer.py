from admin_manage_banners.models import AwBanners
from rest_framework import serializers



class BannerSerializer(serializers.ModelSerializer):
	class Meta:
		model = AwBanners
		fields = ['id', 'Title', 'Type', 'Image', 'Description', 'Status']
		depth = 2