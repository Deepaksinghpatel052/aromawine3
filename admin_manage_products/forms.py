from django import forms
from .models import AwProducts,AwWineType
from admin_manage_producer.models import AwProducers
from admin_manage_country.models import AwCountry
from admin_manage_region.models import AwRegion
from admin_manage_color.models import AwColor
from admin_manage_size.models import AwSize

class AwProductsForm(forms.ModelForm):
    Product_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Product_name', 'placeholder': "Enter your product name"}))
    Meta_Title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Meta_Title', 'placeholder': "Enter your Meta Title"}))
    Meta_Keyword = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Meta_Keyword', 'placeholder': "Enter your Meta Keyword"}))
    Select_Type = forms.ModelChoiceField(required=True, empty_label="Please select type", queryset=AwWineType.objects.filter(Status=True), widget=forms.Select(attrs={"class": "form-control" ,'name': 'Country'}))
    Producer = forms.ModelChoiceField(required=True ,empty_label="Please select producer",  queryset=AwProducers.objects.filter(Status=True), widget=forms.Select(attrs={"class": "form-control" ,'name': 'Country'}))
    Producer = forms.ModelChoiceField(required=True, empty_label="Please select producer", queryset=AwProducers.objects.filter(Status=True), widget=forms.Select(attrs={"class": "form-control" ,'name': 'Country'}))
    Country = forms.ModelChoiceField(required=True,empty_label="Please select country",  queryset=AwCountry.objects.filter(Status=True), widget=forms.Select(attrs={"class": "form-control" ,'name': 'Country'}))
    Regions = forms.ModelChoiceField(required=True, empty_label="Please select regions", queryset=AwRegion.objects.filter(Status=True), widget=forms.Select(attrs={"class": "form-control" ,'name': 'Country'}))

    Color = forms.ModelChoiceField(required=True, empty_label="Please select Color",
                                     queryset=AwColor.objects.filter(Status=True),
                                     widget=forms.Select(attrs={"class": "form-control", 'name': 'Color'}))
    Bottel_Size = forms.ModelChoiceField(required=True, empty_label="Please select Bottel Size",
                                     queryset=AwSize.objects.filter(Status=True),
                                     widget=forms.Select(attrs={"class": "form-control", 'name': 'Bottel_Size'}))
    Description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "summernote_text form-control des", "placeholder": "Description", 'name': 'Description'}))
    Meta_Description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control des", "placeholder": "summernote_text", 'name': 'summernote_text'}))

    class Meta:
        model = AwProducts
        fields = ['Select_Type','Product_name','Producer','Category','Color','Appellation','Bottel_Size','Classification','Vintage','Varietals','Country','Regions','Grape','Description','Meta_Title','Meta_Keyword','Meta_Description']