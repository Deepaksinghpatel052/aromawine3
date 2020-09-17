from rest_framework import serializers
from .models import AwAdminSetting


class ApiWineProjectInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = AwAdminSetting
        fields = ('id', 'Project_Name','Project_Tag_Line','Logo','favicon','Duty','GST','Analytics','Manage_Delivery_Countries','Facebook','Twitter','Linkedin','Instgram','Google','Yelp')