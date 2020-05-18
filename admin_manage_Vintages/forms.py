from django import forms
from .models import AwVintages

class AwVintagesForm(forms.ModelForm):
    Vintages_Year = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'Vintages_Year', 'placeholder': "Enter your Vintages year"}))

    class Meta:
        model = AwVintages
        fields = ['Vintages_Year','Set_To']