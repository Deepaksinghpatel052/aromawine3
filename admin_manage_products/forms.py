from django import forms
from .models import AwProducts,AwWineType
from admin_manage_producer.models import AwProducers
from admin_manage_country.models import AwCountry
from admin_manage_region.models import AwRegion
from admin_manage_color.models import AwColor
from admin_manage_size.models import AwSize
from wine_palate.models import AwWinePalateFlavors
from admin_manage_appellation.models import AwAppellation
from admin_manage_classification.models import AwClassification
from admin_manage_categoryes.models import AwCategory
from wine_palate.models import AwWinePalateFlavors
from admin_manage_Vintages.models import AwVintages
from admin_manage_grape.models import AwGrape
from admin_manage_varietals.models import AwVarietals
from admin_manage_food_pair.models import AwFoodpair

class AwProductsForm(forms.ModelForm):
    Product_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Product_name', 'placeholder': "Enter your product name"}))
    LWineCode = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'LWineCode', 'placeholder': "Enter your LWine Code"}))
    AlcoholPercentage = forms.CharField(required=False, widget=forms.NumberInput(attrs={"class": "form-control","value":"0", 'name': 'AlcoholPercentage', 'placeholder': "Alcohol Percentage"}))
    Analytical_date = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Analytical_date', 'placeholder': "Analytical Data"}))
    Meta_Title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Meta_Title', 'placeholder': "Enter your Meta Title"}))
    Meta_Keyword = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'name': 'Meta_Keyword', 'placeholder': "Enter your Meta Keyword"}))
    Select_Type = forms.ModelChoiceField(required=True, empty_label="Please select type", queryset=AwWineType.objects.filter(Status=True).order_by("Type"), widget=forms.Select(attrs={"class": "form-control" ,'name': 'Country'}))
    Producer = forms.ModelChoiceField(required=True ,empty_label="Please select producer",  queryset=AwProducers.objects.filter(Status=True).order_by("Winnery_Name"), widget=forms.Select(attrs={"class": "form-control" ,'name': 'Country'}))
    # Producer = forms.ModelChoiceField(required=True, empty_label="Please select producer", queryset=AwProducers.objects.filter(Status=True), widget=forms.Select(attrs={"class": "form-control" ,'name': 'Country'}))
    Country = forms.ModelChoiceField(required=True,empty_label="Please select country",  queryset=AwCountry.objects.filter(Status=True).order_by("Country_Name"), widget=forms.Select(attrs={"class": "form-control" ,'name': 'Country'}))
    Regions = forms.ModelChoiceField(required=True, empty_label="Please select regions", queryset=AwRegion.objects.filter(Status=True).order_by("Region_Name"), widget=forms.Select(attrs={"class": "form-control" ,'name': 'Country'}))
    # Flavours = forms.ModelChoiceField(required=False, empty_label="Please select Flavours", queryset=AwWinePalateFlavors.objects.all(), widget=forms.Select(attrs={"class": "form-control" ,'name': 'Flavours'}))

    Color = forms.ModelChoiceField(required=True, empty_label="Please select Color",queryset=AwColor.objects.filter(Status=True).order_by("Color_name"),widget=forms.Select(attrs={"class": "form-control", 'name': 'Color'}))
    # Bottel_Size = forms.ModelChoiceField(required=True, empty_label="Please select Bottel Size",
    #                                  queryset=AwSize.objects.filter(Status=True).order_by("Bottle_Size"),widget=forms.Select(attrs={"class": "form-control", 'name': 'Bottel_Size'}))
    Description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "summernote_text form-control des", "placeholder": "Description", 'name': 'Description'}))
    Meta_Description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control des", "placeholder": "summernote_text", 'name': 'summernote_text'}))

    class Meta:
        model = AwProducts
        fields = ['Select_Type','LWineCode','AlcoholPercentage','Product_name','Producer','Category','Flavours','Color','Appellation','Bottel_Size','Classification','Vintage',
                  'Varietals','Country','Regions','Grape','Description','Meta_Title','Meta_Keyword','Meta_Description','Analytical_date','FoodPair']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Category'].queryset = AwCategory.objects.filter(Status=True).order_by("Category_name")
        self.fields['Appellation'].queryset = AwAppellation.objects.filter(Status=True).order_by("Appellation_Name")
        self.fields['Classification'].queryset = AwClassification.objects.filter(Status=True).order_by("Classification_Name")
        self.fields['Flavours'].queryset = AwWinePalateFlavors.objects.all().order_by("Type")
        self.fields['Vintage'].queryset = AwVintages.objects.filter(Status=True).order_by("Vintages_Year")
        self.fields['Varietals'].queryset = AwVarietals.objects.filter(Status=True).order_by('Varietals_Name')
        self.fields['FoodPair'].queryset = AwFoodpair.objects.filter(Status=True).order_by('Food_Pair_Name')
        self.fields['Grape'].queryset = AwGrape.objects.filter(Status=True).order_by('Grape_Name')
        self.fields['Bottel_Size'].queryset = AwSize.objects.filter(Status=True).order_by("Bottle_Size")
