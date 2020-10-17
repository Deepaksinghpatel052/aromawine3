from django import forms
from .models import AwAdminSetting, AwAllCountry , AwManageShipping
from admin_manage_country.models import AwCountryUser



class AwAdminSettingForm(forms.ModelForm):
    Project_Name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Product_name', 'placeholder': "Enter your Project name"}))
    Project_Tag_Line = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Product_name', 'placeholder': "Enter your Project Tag Line"}))
    Duty = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'Product_name', 'placeholder': "Enter Product Duty"}))
    GST = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'Product_name', 'placeholder': "Enter Product Duty"}))
    Analytics = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control des", "placeholder": "Description", 'name': 'Description'}))
    Facebook = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control des", "placeholder": "Facebook Page URL"}))
    Twitter = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control des", "placeholder": "Twitter Page URL"}))
    Linkedin = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control des", "placeholder": "Twitter Page URL"}))
    Instgram = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control des", "placeholder": "Instgram Page URL"}))
    Google = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control des", "placeholder": "Google Page URL"}))
    Yelp = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control des", "placeholder": "Yelp Page URL"}))
    EMAIL_HOST = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control des", "placeholder": "EMAIL HOST"}))
    EMAIL_PORT = forms.CharField(required=False, widget=forms.NumberInput(attrs={"class": "form-control des", "placeholder": "EMAIL PORT"}))
    EMAIL_HOST_USER = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control des", "placeholder": "EMAIL HOST USER"}))
    EMAIL_HOST_PASSWORD = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control des", "placeholder": "EMAIL HOST PASSWOR"}))


    class Meta:
        model = AwAdminSetting
        fields = ['Project_Name', 'Project_Tag_Line', 'Logo', 'favicon', 'Duty', 'GST', 'Analytics',
                  'Manage_Delivery_Countries', 'Facebook', 'Twitter', 'Linkedin', 'Instgram', 'Google', 'Yelp', 'EMAIL_HOST',
                  'EMAIL_USE_TLS', 'EMAIL_PORT','EMAIL_HOST_USER','EMAIL_HOST_PASSWORD']



class AwManageShippingForm(forms.ModelForm):
    Country = forms.ModelChoiceField(required=True, empty_label="Please select Country",queryset=AwCountryUser.objects.all(),widget=forms.Select(attrs={"class": "form-control", 'name': 'Country'}))
    min_ordr_amount = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'Product_name', 'placeholder': "Min Ordr Amount"}))
    Shiping_Fees_min_order_amount = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'Product_name', 'placeholder': "Free Flat Shipping"}))
    class Meta:
        model = AwManageShipping
        fields = ['Country', 'min_ordr_amount', 'Shiping_Fees_min_order_amount']


