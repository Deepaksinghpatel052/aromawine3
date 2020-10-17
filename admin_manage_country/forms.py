from django import forms
from .models import AwCountry

class AwCountryForm(forms.ModelForm):
    Country_Name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Country_name', 'placeholder': "Enter your Country name"}))
    # Set_To = forms.ModelChoiceField(required=True,  queryset=AwSetTo.objects.filter(Status=True), widget=forms.Select(attrs={"class": "form-control example-multiple-optgroups" ,'name': 'Set_To[]',"multiple":"multiple"}))
    Description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "summernote_text form-control des", "placeholder": "Description", 'name': 'Description'}))

    class Meta:
        model = AwCountry
        fields = ['Country_Name','Set_To','Description','Banner_Image']