from django import forms
from home.models import AwCmsPaage

class AwCmsPaageForm(forms.ModelForm):
    Title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Page_name', 'placeholder': "Enter your Page name."}))
    Slug = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Slug', 'placeholder': "Enter your Page Slug."}))
    Short_description = forms.CharField(required=False, widget=forms.Textarea( attrs={"class": "form-control des", "placeholder": "Description", 'name': 'Description'}))
    description = forms.CharField(required=False, widget=forms.Textarea( attrs={"class": "summernote_text form-control des", "placeholder": "Description", 'name': 'Description'}))

    class Meta:
        model = AwCmsPaage
        fields = ['Title','description','Background_Image','Short_description','Slug','Short_description_Show_in_Footer','Publish']