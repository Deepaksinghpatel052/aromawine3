from django import forms
from .models import AwEvent,AwEventType


class DateInput(forms.DateInput):
    input_type = 'date'

class AwEventForm(forms.ModelForm):
    Event_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", 'name': 'Event_name', 'placeholder': "Enter your event name"}))
    Event_Host = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", 'name': 'Event_name', 'placeholder': "Enter your Host name"}))
    Description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={"class": "summernote_text form-control des", "placeholder": "Description", 'name': 'Description'}))
    Short_Description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={"class": " form-control des", "placeholder": "Description", 'name': 'Description'}))
    Producer_Notes = forms.CharField(required=False, widget=forms.Textarea(
        attrs={"class": " form-control des summernote_text", "placeholder": "Producer Notes", 'name': 'Producer_Notes'}))
    Start_Date = forms.DateField(widget=DateInput)
    End_Date = forms.DateField(widget=DateInput)
    ticket_pr_person = forms.CharField(widget=forms.NumberInput(
        attrs={"class": "form-control", 'name': 'End_Date', 'placeholder': "ticket pr person"}))
    Event_Type = forms.ModelChoiceField(required=True, empty_label="Please select type",
                                         queryset=AwEventType.objects.all(),
                                         widget=forms.Select(attrs={"class": "form-control", 'name': 'Country'}))
    ticket_price = forms.CharField(widget=forms.NumberInput(
        attrs={"class": "form-control", 'name': 'ticket_price', 'placeholder': "Ticket price"}))

    Location = forms.CharField(required=False, widget=forms.Textarea(
        attrs={"class": "summernote_text form-control des", "placeholder": "Location", 'name': 'Location'}))
    class Meta:
        model = AwEvent
        fields = ['Event_name','Event_Type','Event_Host','Event_Type','Description','Short_Description','Producer_Notes','Location','Start_Date','End_Date','ticket_pr_person','ticket_price','Status']
        # widgets = {
        #     'Start_Date': DateInput()
        # }