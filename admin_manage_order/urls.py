from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageOrdersView.as_view(),name="orders"),
    path('celler-order', views.CellerOrder.as_view(),name="celler_order"),
    path('refunded-order', views.RefundedOrder.as_view(),name="refunded_order"),
    path('canclled-order', views.CanclledOrder.as_view(),name="canclled_order"),
    path('failled-order', views.FailledOrder.as_view(),name="failled_order"),


    path('<str:id>', views.EditOrder.as_view(),name="edit_order"),
    path('<str:id>/cancel-order', views.CancelOrder.as_view(),name="cancel_order"),
    path('<str:id>/change-order-status', views.ChangeOrderStatus.as_view(),name="change_order_status"),


    path('<pk>/edit-address', views.EditAddress.as_view(),name="edit_address"),

]