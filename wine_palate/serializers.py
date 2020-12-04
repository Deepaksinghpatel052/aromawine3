
from rest_framework import serializers
from .models import AwWinePalateFlavors,AwWinePalateCategories

class AwWinePalateCategoriesSerializear(serializers.ModelSerializer):
    class Meta:
        model = AwWinePalateFlavors
        fields = ['id', 'Category_name', 'Category_Color']
        depth = 2


class AwWinePalateFlavorsSerializear(serializers.ModelSerializer):
    class Meta:
        model = AwWinePalateFlavors
        fields = ['id', 'Category', 'Type']
        depth = 2