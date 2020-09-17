from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.WishListVidw.as_view(), name="user_wishlist"),
    # path('add-appellation', views.CreateAppellationView.as_view(),name="add_appellation"),
    path('add-wishlist/<slug:product_id>/<slug:vintage_year>', views.add_product_in_wishlist, name="add_wishlist"),
]