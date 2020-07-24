from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrederVidw.as_view(),name="orders"),
    path('<slug:order_id>/product-info', views.ProoductInfoView.as_view(),name="prodyuct_info"),
    path('checkout', views.CheckOutView.as_view(),name="checkout"),
    path('my-card', views.MyCardView.as_view(),name="my_card"),
    path('update-card', views.update_card,name="update_card"),
    path('check-coupon-code', views.check_coupon_code,name="check_coupon_code"),

    path('<pk>/remove-product-from-card', views.remove_product_from_card,name="remove_product_from_card"),
    path('get-product-proce', views.get_product_price, name="get_product_price"),
    path('add-to-card', views.add_to_card, name="add_to_card"),
    path('get-card-product', views.get_my_card_product, name="get_my_card_product"),
    path('get-product-list', views.get_product_list, name="get_product_list"),

]