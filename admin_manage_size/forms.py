from django import forms
from .models import AwSize

class AAwSizeForm(forms.ModelForm):
    Bottle_Size = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Bottle_Size', 'placeholder': "Enter your Bottle name"}))

    class Meta:
        model = AwSize
        fields = ['Bottle_Size']