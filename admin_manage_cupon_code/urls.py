from django.urls import path
from . import views

urlpatterns = [
    path('', views.ManageCouponView.as_view(),name="admin_manage_cupon_code"),
    path('add-coupon', views.CreateCouponView.as_view(),name="add_coupon"),
    path('<pk>/update-coupon', views.CouponUpdateView.as_view(),name="update_coupon"),
    path('<pk>/dekete-coupon', views.CouponDeleteView.as_view(),name="delete_coupon"),

]