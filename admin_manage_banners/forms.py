from django import forms
from .models import AwBanners


GEEKS_CHOICES =(
    ("Home Banner", "Home Banner"),
    ("Special offer", "Special offer"),
    ("About Aroma", "About Aroma"),
)

class AwBannersForm(forms.ModelForm):
    Title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Categorye_name', 'placeholder': "Enter your Categorye name."}))
    Type = forms.ChoiceField(choices = GEEKS_CHOICES,help_text="Select Type",error_messages={"required":"Please select type","invalid_choice":"PLease select a valid type"} ,widget=forms.Select(attrs={"class": "form-control"}))
    Description = forms.CharField(required=False, widget=forms.Textarea( attrs={"class": "summernote_text form-control des", "placeholder": "Description", 'name': 'Description'}))

    class Meta:
        model = AwBanners
        fields = ['Title', 'Type',  'Description']



