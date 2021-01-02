from django import forms
from .models import AwNotification
from django.contrib.auth.models import User


class AwNotificationForm(forms.ModelForm):
    user = forms.ModelChoiceField(required=True, empty_label="Please select User",queryset=User.objects.all().order_by('username'),widget=forms.Select(attrs={"class": "form-control", 'name': 'User_Type'}))
    Description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "summernote_text form-control des", "placeholder": "Description", 'name': 'Description'}))

    class Meta:
        model = AwNotification
        fields = ['user', 'Description']