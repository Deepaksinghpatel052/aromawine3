from rest_framework import serializers
import django
from rest_framework.authtoken.models import Token
from .models import AwCategory



class DfCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = AwCategory
        fields = ('id', 'Category_name','Title','Image','Description','Status')
        depth = 2
