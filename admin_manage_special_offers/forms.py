from django import forms
from .models import AwSpecialOffers

class AwSpecialOffersForm(forms.ModelForm):
    Title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Title', 'placeholder': "Enter your Title"}))
    Priority_set = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'Priority_set', 'placeholder': "Enter your Priority Set"}))
    Description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", 'name': 'Description', 'placeholder': "Enter your Description"}))
    Link = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Link', 'placeholder': "Enter your Link"}))

    class Meta:
        model = AwSpecialOffers
        fields = ['Title','Priority_set','Description','Banner_Image','Link']