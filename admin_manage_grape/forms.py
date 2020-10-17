from django import forms
from .models import AwGrape


class AwGrapeForm(forms.ModelForm):
    Grape_Name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Grape_Name', 'placeholder': "Enter your grape name"}))
    Short_Description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control des", "placeholder": "Description", 'name': 'Short Description'}))
    Description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "summernote_text form-control des", "placeholder": "Description", 'name': 'Description'}))

    class Meta:
        model = AwGrape
        fields = ['Grape_Name','Grape_Image','Short_Description','Description','banner_Image']