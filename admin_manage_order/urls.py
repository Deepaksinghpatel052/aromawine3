from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageOrdersView.as_view(),name="orders"),
    path('caller', views.ManageOrdersCallerView.as_view(),name="caller"),
    path('delivery', views.ManageOrdersDeliveryView.as_view(),name="delivery"),
    path('<slug:type>', views.ManageOrdersAccordingToTypeView.as_view(),name="orders_type"),
    path('edit-order/<slug:order_id>', views.EditOrdersView.as_view(),name="edit_order"),
    path('delete-note/<slug:id>/<slug:order_id>', views.delete_note,name="delete_note"),
    path('update-order-status/<slug:order_id>/<slug:status>', views.order_status_update,name="order_status_update")

]