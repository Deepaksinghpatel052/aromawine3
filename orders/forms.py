from django import forms
from orders.models import AwOrderNote


class AwOrderNoteForm(forms.ModelForm):
    Note = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Note", 'name': 'Address', "rows": "4"}))
    class Meta:
        model = AwOrderNote
        fields = ['Note','Attachment','Display_Status']


