from django.urls import path
from . import views

urlpatterns = [
    path('', views.CellarVidw.as_view(),name="manage_cellar"),

]