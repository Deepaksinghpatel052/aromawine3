from django import forms
from .models import AwAppellation
from admin_manage_country.models import AwCountry
from admin_manage_producer.models import AwSetTo

class AwAppellationForm(forms.ModelForm):
    Appellation_Name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Appellation_Name', 'placeholder': "Enter your appellation name"}))

    class Meta:
        model = AwAppellation
        fields = ['Appellation_Name','Country','Set_To']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Country'].queryset = AwCountry.objects.filter(Status=True).order_by("Country_Name")
        self.fields['Set_To'].queryset = AwSetTo.objects.filter(Status=True).order_by("Title")