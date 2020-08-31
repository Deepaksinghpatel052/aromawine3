from django import forms
from .models import AwPaymentMethod


class DateInput(forms.DateInput):
    input_type = 'date'


class AwPaymentMethodForm(forms.ModelForm):

    Name_on_Card = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Name_on_Card', 'placeholder': "Name on Card"}))
    Card_Number = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Card_Number', 'placeholder': "Card number" ,"maxlength":"16"}))
    CVC_CVV = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'CVC_CVV', 'placeholder': "CVC/CVV" ,"maxlength":"3"}))
    ZIP = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'ZIP', 'placeholder': "ZIP Code" ,"maxlength":"6"}))
    Expiry_Date = forms.DateField(widget=DateInput)

    class Meta:
        model = AwPaymentMethod
        fields = ['Name_on_Card', 'Card_Number', 'Expiry_Date','CVC_CVV', 'ZIP', 'Paypal','Pay_on_delivery','active_status']

