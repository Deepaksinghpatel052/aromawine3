from django import forms
from .models import AwSetTo,AwProducers

class AwProducersForm(forms.ModelForm):
    Winnery_Name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Winnery_Name', 'placeholder': "Enter your winery name"}))
    # Set_To = forms.ModelChoiceField(required=True,  queryset=AwSetTo.objects.filter(Status=True), widget=forms.Select(attrs={"class": "form-control example-multiple-optgroups" ,'name': 'Set_To[]',"multiple":"multiple"}))
    Short_Description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control des", "placeholder": "Description", 'name': 'Short Description'}))
    Description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "summernote_text form-control des", "placeholder": "Description", 'name': 'Description'}))

    class Meta:
        model = AwProducers
        fields = ['Winnery_Name','Set_To','Producer_Image','Short_Description','Description']