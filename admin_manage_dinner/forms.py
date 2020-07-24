from django import forms
from .models import AwDinner


class AwDinnerForm(forms.ModelForm):
    Dinner_Name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Dinner_Name', 'placeholder': "Enter your dinner name"}))
    # Set_To = forms.ModelChoiceField(required=True,  queryset=AwSetTo.objects.filter(Status=True), widget=forms.Select(attrs={"class": "form-control example-multiple-optgroups" ,'name': 'Set_To[]',"multiple":"multiple"}))
    Short_Description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control des", "placeholder": "Short Description", 'name': 'ShortDescription'}))
    Description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "summernote_text form-control des", "placeholder": "Description", 'name': 'Description'}))

    class Meta:
        model = AwDinner
        fields = ['Dinner_Name', 'Wine_With_Dienner', 'Dinner_Image','Short_Description', 'Description']