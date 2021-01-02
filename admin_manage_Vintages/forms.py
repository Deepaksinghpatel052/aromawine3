from django import forms
from .models import AwVintages
from admin_manage_producer.models import AwSetTo

class AwVintagesForm(forms.ModelForm):
    Vintages_Year = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'Vintages_Year', 'placeholder': "Enter your Vintages year"}))

    class Meta:
        model = AwVintages
        fields = ['Vintages_Year','Set_To']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Set_To'].queryset = AwSetTo.objects.filter(Status=True).order_by("Title")