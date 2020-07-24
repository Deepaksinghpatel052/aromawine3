from django import forms
from .models import AwTesting


class AwTestingForm(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Name', 'placeholder': "Enter your Name"}))
    # Set_To = forms.ModelChoiceField(required=True,  queryset=AwSetTo.objects.filter(Status=True), widget=forms.Select(attrs={"class": "form-control example-multiple-optgroups" ,'name': 'Set_To[]',"multiple":"multiple"}))
    Short_Description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control des", "placeholder": "Short Description", 'name': 'ShortDescription'}))
    Description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "summernote_text form-control des", "placeholder": "Description", 'name': 'Description'}))

    class Meta:
        model = AwTesting
        fields = ['Name', 'Wine_With_Testing', 'Testing_Image','Short_Description', 'Description']