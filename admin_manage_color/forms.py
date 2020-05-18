from django import forms
from .models import AwColor


class AwColorForm(forms.ModelForm):
    Color_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Color_name', 'placeholder': "Enter your Color_name."}))
    Description = forms.CharField(required=False, widget=forms.Textarea( attrs={"class": "summernote_text form-control des", "placeholder": "Description", 'name': 'Description'}))

    class Meta:
        model = AwColor
        fields = ['Color_name', 'Description']