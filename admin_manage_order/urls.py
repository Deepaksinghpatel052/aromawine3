from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageOrdersView.as_view(),name="orders"),
    path('cellar/', views.ManageOrdersCallerView.as_view(),name="caller"),
    path('product-sales-list/', views.ManageProductSalesListView.as_view(),name="product_sales_list"),
    path('delivery/', views.ManageOrdersDeliveryView.as_view(),name="delivery"),
    path('ticket/', views.ManageOrdersTicketView.as_view(),name="ticket"),
    path('<slug:type>', views.ManageOrdersAccordingToTypeView.as_view(),name="orders_type"),

    path('complete/cellar/', views.ManageOrdersAccordingToConplateCellar.as_view(),name="complate_cellar"),
    path('complete/delivery/', views.ManageOrdersAccordingToConplateDelivery.as_view(),name="complate_delivery"),

    path('edit-order/<slug:order_id>', views.EditOrdersView.as_view(),name="edit_order"),
    path('delete-note/<slug:id>/<slug:order_id>', views.delete_note,name="delete_note"),
    path('update-order-status/<slug:order_id>/<slug:status>', views.order_status_update,name="order_status_update")
]