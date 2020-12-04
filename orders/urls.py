from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrederVidw.as_view(),name="orders"),
    path('<slug:order_id>/product-info', views.ProoductInfoView.as_view(),name="prodyuct_info"),
    path('checkout', views.CheckOutView.as_view(),name="checkout"),
    path('checkout/<slug:order_id>', views.CheckOutView.as_view(),name="checkout"),
    path('invoice/<slug:order_id>', views.OrderInvoiceView.as_view(),name="invoice"),
    path('get_shipping_charge', views.get_shipping_charge,name="get_shipping_charge"),
    path('get_country_id', views.get_country_id,name="get_country_id"),
    path('my-cart', views.MyCardView.as_view(),name="my_card"),
    path('update-card', views.update_card,name="update_card"),
    path('check-coupon-code', views.check_coupon_code,name="check_coupon_code"),
    path('<pk>/remove-product-from-card', views.remove_product_from_card,name="remove_product_from_card"),
    path('get-product-proce', views.get_product_price, name="get_product_price"),
    path('add-to-card', views.add_to_card, name="add_to_card"),
    path('get-card-product', views.get_my_card_product, name="get_my_card_product"),
    path('get-product-list', views.get_product_list, name="get_product_list"),
    # ======================================================================
    path('add-to-card/api', views.add_to_card_api.as_view(),name="product_detail_api"),
    path('get-card-product-api', views.get_my_card_product_api.as_view(), name="get_my_card_product_api"),
    path('remove-product-from-card-api', views.remove_product_from_card_api.as_view(),name="remove_product_from_card_api"),
    path('update-card-api', views.update_card_api.as_view(),name="update_card_api"),
    path('check-coupon-code-api', views.check_coupon_code_api.as_view(),name="check_coupon_code_api"),
    path('cookies-to-user-id-api', views.cookies_to_user_id.as_view(),name="cookies_to_user_id"),

    path('get-product-one-case-formate-price-api', views.get_product_price_api.as_view(), name="get_product_price_api"),
    path('get-shipping-charge-api', views.get_shipping_charge_api.as_view(),name="get_shipping_charge_api"),
    path('get-user-address-list-api', views.get_user_address_list_api.as_view(),name="get_user_address_list_api"),
    path('checkout-api', views.CheckOutViewApi.as_view(),name="checkoutApi"),
    path('update-order-api', views.UdateOrderApi.as_view(),name="UdateOrderApi"),
    path('get-order-info-api', views.GetOrderInfoApi.as_view(),name="GetOrderInfoApi"),
]