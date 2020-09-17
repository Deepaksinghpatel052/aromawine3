from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ManageWinePalateView.as_view(), name="wine_palate"),
]