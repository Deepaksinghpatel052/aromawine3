from django.shortcuts import render
from django.views import generic
# Create your views here.


class ManageWinePalateView(generic.TemplateView):
    template_name = "web/wine_palate/wine_palate.html"