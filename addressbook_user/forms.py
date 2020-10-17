from django import forms
from .models import AwAddressBook
from admin_manage_country.models import AwCountryUser
from admin_manage_setting.models import AwManageShipping

class AwAddressBookForm(forms.ModelForm):

    First_Name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'First_Name', 'placeholder': "Enter Your First Name."}))
    Last_Name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Last_Name', 'placeholder': "Enter Your Last Name."}))
    Email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Email', 'placeholder': "Enter Your Email."}))
    Pnone_no = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'Pnone_no', 'placeholder': "Enter Your Pnone no."}))
    Conpany_Name = forms.CharField(required=False,widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Conpany_Name', 'placeholder': "Enter Your Company Name."}))
    Country = forms.ModelChoiceField(required=True, empty_label="Please Select Country", queryset=AwManageShipping.objects.all().order_by('Country'), widget=forms.Select(attrs={"class": "form-control" ,'name': 'Conpany_Name'}))
    City = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'City', 'placeholder': "Enter Your City."}))
    State = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'State', 'placeholder': "Enter Your State."}))
    Address = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Address", 'name': 'Address',"rows":"5"}))
    Address_2 = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Address_2", 'name': 'Address',"rows":"5"}))
    Postcode = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'Postcode', 'placeholder': "Enter Your Postcode."}))
    Landmark = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Landmark', 'placeholder': "Enter Your Landark."}))

    class Meta:
        model = AwAddressBook
        fields = ['First_Name', 'Last_Name','State',  'Email','Pnone_no','Conpany_Name','Country','Address','Address_2','City','Postcode','Landmark']


class AwAddressBookFormUser(forms.ModelForm):
    First_Name = forms.CharField(required=False,widget=forms.TextInput(attrs={"class": "form-control", 'name': 'First_Name', 'placeholder': "Enter Your First Name."}))
    Last_Name = forms.CharField(required=False,widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Last_Name', 'placeholder': "Enter Your Last Name."}))
    Email = forms.CharField(required=False,widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Email', 'placeholder': "Enter Your Email."}))
    Pnone_no = forms.CharField(required=False,widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'Pnone_no', 'placeholder': "Enter Your Pnone no."}))
    Conpany_Name = forms.CharField(required=False,widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Conpany_Name', 'placeholder': "Enter Your Company Name."}))
    Country = forms.ModelChoiceField(required=False, empty_label="Please Select Country", queryset=AwManageShipping.objects.all().order_by('Country'), widget=forms.Select(attrs={"class": "form-control" ,'name': 'Conpany_Name'}))
    City = forms.CharField(required=False,widget=forms.TextInput(attrs={"class": "form-control", 'name': 'City', 'placeholder': "Enter Your City."}))
    State = forms.CharField(required=False,widget=forms.TextInput(attrs={"class": "form-control", 'name': 'State', 'placeholder': "Enter Your State."}))
    Address = forms.CharField(required=False,widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Address", 'name': 'Address',"rows":"5"}))
    Address_2 = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Address_2", 'name': 'Address',"rows":"5"}))
    Postcode = forms.CharField(required=False,widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'Postcode', 'placeholder': "Enter Your Postcode."}))
    Landmark = forms.CharField(required=False,widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Landark', 'placeholder': "Enter Your Landmark."}))

    class Meta:
        model = AwAddressBook
        fields = ['First_Name', 'Last_Name','State',  'Email','Pnone_no','Conpany_Name','Country','Address','Address_2','City','Postcode','Landmark']