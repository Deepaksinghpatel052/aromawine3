from django import forms
from .models import AwFoodpair


class AwFoodpairForm(forms.ModelForm):
    Food_Pair_Name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Food Pair Name','placeholder': "Enter your food pair name"}))

    class Meta:
        model = AwFoodpair
        fields = ['Food_Pair_Name']