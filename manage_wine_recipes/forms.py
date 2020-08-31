from django import forms
from .models import AwWineRecipes
from admin_manage_products.models import AwProducts

class DateInput(forms.DateInput):
    input_type = 'date'

class AwRecipesForm(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", 'name': 'Event_name', 'placeholder': "Enter your event name"}))
    Description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={"class": "summernote_text form-control des", "placeholder": "Description", 'name': 'Description'}))
    Short_Description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={"class": " form-control des", "placeholder": "Description", 'name': 'Description'}))
    class Meta:
        model = AwWineRecipes
        fields = ['Name','Wine_With_Recipes','Short_Description','Description','Status']
        # widgets = {
        #     'Start_Date': DateInput()
        # }