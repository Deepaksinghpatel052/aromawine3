from django import forms
from wine_palate.models import AwWinePalateFlavors,AwWinePalateCategories


class AwFlavorsForm(forms.ModelForm):
    Category = forms.ModelChoiceField(required=True, empty_label="Please select Category",queryset=AwWinePalateCategories.objects.all(),widget=forms.Select(attrs={"class": "form-control", 'name': 'Color'}))
    Type = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Type', 'placeholder': "Enter Flavors name"}))

    class Meta:
        model = AwWinePalateFlavors
        fields = ['Category','Type']