from django import forms
from .models import AwCuponCode


CHOICES=[('P','In Percent'),('A','In Amount')]



class DateInput(forms.DateInput):
    input_type = 'date'

class AwCouponForm(forms.ModelForm):
    Type = forms.ChoiceField(label='Type', choices=CHOICES,required=True)
    Amount = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'Country_name', 'placeholder': "Enter Amount"}))
    Usage_Limit_Per_Coupon = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'Country_name', 'placeholder': "Use Limit"}))
    Usage_Limit_Per_User = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control", 'name': 'Country_name', 'placeholder': "Use Limit pr user"}))
    Valid_from = forms.DateField(widget=DateInput)
    Valid_to = forms.DateField(widget=DateInput)

    class Meta:
        model = AwCuponCode
        fields = ['Type','Amount','Usage_Limit_Per_Coupon','Usage_Limit_Per_User','Valid_from','Valid_to','Status']