from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageCustomerView.as_view(),name="customer"),
    path('<slug:id>/get-user-prefrence', views.ManagePrefrenceView.as_view(), name="user_preferance"),
    path('<slug:id>/get-user-info', views.ManageUserInfoView.as_view(), name="user_info"),
    path('<slug:id>/get-user-order-history', views.ManageUserOrderHistoryView.as_view(), name="user_order_history"),
]