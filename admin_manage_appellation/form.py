from django import forms
from .models import AwAppellation

class AwAppellationForm(forms.ModelForm):
    Appellation_Name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Appellation_Name', 'placeholder': "Enter your appellation name"}))

    class Meta:
        model = AwAppellation
        fields = ['Appellation_Name','Country','Set_To']