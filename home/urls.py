from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(),name="home"),
    path('page/<slug:title>', views.CustomPageView.as_view(),name="custom_page"),
]