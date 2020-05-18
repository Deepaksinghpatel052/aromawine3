from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_login

urlpatterns = [
    path('', views.AdminDashboardVIew.as_view(),name="dashboard"),
    path('login/', auth_login.LoginView.as_view(template_name='admin/login/index.html')),
]

