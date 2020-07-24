from django import forms
from .models import Service_Interests,AwInterestType


class AwServiceInterestsForm(forms.ModelForm):
    Service_interests_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Service_interests_name', 'placeholder': "Enter Service Interests"}))
    Select_Type = forms.ModelChoiceField(required=True, empty_label="Please select type", queryset=AwInterestType.objects.filter(Status=True), widget=forms.Select(attrs={"class": "form-control" ,'name': 'interest_type'}))

    class Meta:
        model = Service_Interests
        fields = ['Service_interests_name','Select_Type']

