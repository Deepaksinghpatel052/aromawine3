from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrederVidw.as_view(),name="orders"),
    path('checkout', views.CheckOutView.as_view(),name="checkout"),
    path('get-product-proce', views.get_product_price, name="get_product_price"),
    path('add-to-card', views.add_to_card, name="add_to_card"),
    path('get-card-product', views.get_my_card_product, name="get_my_card_product"),
    path('get-product-list', views.get_product_list, name="get_product_list"),
]