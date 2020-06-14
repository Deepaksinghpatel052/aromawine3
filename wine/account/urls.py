from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccountCraetLoginView.as_view(),name="account"),
    path('logout', views.LogoutView.as_view(),name="logout"),
]