from django import forms
from .models import AwRegion
from admin_manage_country.models import AwCountry

class AwRegionForm(forms.ModelForm):
    Region_Name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Region_Name', 'placeholder': "Enter your region name"}))
    Country = forms.ModelChoiceField(required=True,empty_label="Please select country",  queryset=AwCountry.objects.filter(Status=True), widget=forms.Select(attrs={"class": "form-control" ,'name': 'Country'}))
    Short_Description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control des", "placeholder": "Description", 'name': 'Short Description'}))
    Description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "summernote_text form-control des", "placeholder": "Description", 'name': 'Description'}))

    class Meta:
        model = AwRegion
        fields = ['Country','Region_Name','Set_To','Region_Image','Short_Description','Description','banner_Image']