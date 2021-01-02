from django import forms
from .models import AwCountry
from admin_manage_producer.models import AwSetTo

class AwCountryForm(forms.ModelForm):
    Country_Name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Country_name', 'placeholder': "Enter your Country name"}))
    # Set_To = forms.ModelChoiceField(required=True,  queryset=AwSetTo.objects.filter(Status=True), widget=forms.Select(attrs={"class": "form-control example-multiple-optgroups" ,'name': 'Set_To[]',"multiple":"multiple"}))
    Description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "summernote_text form-control des", "placeholder": "Description", 'name': 'Description'}))
    Short_Description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control des", "placeholder": "Description", 'name': 'Short Description'}))

    class Meta:
        model = AwCountry
        fields = ['Country_Name','Set_To','Description','Short_Description','Banner_Image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Set_To'].queryset = AwSetTo.objects.filter(Status=True).order_by("Title")