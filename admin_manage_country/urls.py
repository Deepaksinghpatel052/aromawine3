from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageCountryView.as_view(),name="country"),
    path('add-country', views.CreateCountryView.as_view(),name="add_country"),
    path('<pk>/update-country', views.CountryUpdateView.as_view(),name="update_country"),
    path('<pk>/dekete-producer', views.CountryDeleteView.as_view(),name="delete_country"),

]