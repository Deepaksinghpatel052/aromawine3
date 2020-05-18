from django import forms
from .models import AwVarietals

class AwVarietalsForm(forms.ModelForm):
    Varietals_Name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Varietals_Name', 'placeholder': "Enter your varietals name"}))

    class Meta:
        model = AwVarietals
        fields = ['Varietals_Name']