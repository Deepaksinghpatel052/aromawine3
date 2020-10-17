from django.urls import path
from . import views
from knox import views as knox_views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.AccountCraetLoginView.as_view(),name="account"),
    path('logout', views.LogoutView.as_view(),name="logout"),
    path('send_forgate_password_link', views.send_forgate_password_link, name='send_forgate_password_link'),
    path('test_data', views.test_data, name='test_data'),

    path('setcookie', views.setcookie, name='setcookie'),
    path('getcookie', views.getcookie, name='getcookie'),


    # ================ API START ========================
    path('api/register', views.UserRegistration.as_view()),
    path('api/logout', views.ApiLogoutView.as_view(),name="ApiLogout"),
    path('api/login', csrf_exempt(views.ApiLoginView.as_view()),name="Apilogin"),
    path('api/logout', views.ApiLogoutView.as_view(),name="ApiLogout"),
    path('api/get-login-user-info', views.ApiLoginUserInfoView.as_view(),name="login_user_info"),
    # ================ API END ========================

]