from django import forms
from .models import AwMembership


class AwMembershipForm(forms.ModelForm):
    Membership_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Membership_name', 'placeholder': "Enter your Membership name"}))
    min_price = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'min_price', 'placeholder': "Enter your min price"}))
    max_price = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'max_price', 'placeholder': "Enter your max price"}))

    class Meta:
        model = AwMembership
        fields = ['Membership_name','min_price','max_price']