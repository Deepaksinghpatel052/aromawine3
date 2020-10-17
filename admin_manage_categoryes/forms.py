from django import forms
from .models import AwCategory

class AwCategoryesForm(forms.ModelForm):
    Category_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Categorye_name', 'placeholder': "Enter your Categorye name."}))
    Title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Title', 'placeholder': "Enter your Title"}))
    Description = forms.CharField(required=False, widget=forms.Textarea( attrs={"class": "summernote_text form-control des", "placeholder": "Description", 'name': 'Description'}))

    class Meta:
        model = AwCategory
        fields = ['Category_name', 'Title',  'Description','Status']



