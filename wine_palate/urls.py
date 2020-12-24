from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ManageWinePalateView.as_view(), name="wine_palate"),
    path('get_list_of_category', views.GetWinePalatedataView, name="get_wine_palate"),
    path('get_list_of_category_by_name', views.GetWinePalatedataViewByName, name="get_wine_palate_by_name"),
    path('payment', views.payment, name="payment"),
]