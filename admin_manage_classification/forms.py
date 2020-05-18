from django import forms
from .models import AwClassification

class AwClassificationForm(forms.ModelForm):
    Classification_Name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Classification_Name', 'placeholder': "Enter your classification name"}))

    class Meta:
        model = AwClassification
        fields = ['Classification_Name']