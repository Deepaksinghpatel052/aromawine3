from rest_framework import serializers
from .models import AwAddressBook

class AwAddressBookSerializare(serializers.ModelSerializer):
    class Meta:
        model =  AwAddressBook
        fields = ('id', 'First_Name','Last_Name','Email', 'Pnone_no','Conpany_Name', 'Country' ,'Address','Address_2','City','State','Postcode','Landmark')
        depth = 3
