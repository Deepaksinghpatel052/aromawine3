from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManagePerferencesView.as_view(),name="perferences"),
    # path('<slug:prodict_id>/get-cost-and-stock', views.ManageProductCostView.as_view(),name="products_cost"),
    path('add-perferences', views.CreatePerferencesView.as_view(),name="add_perferences"),
    path('<str:id>/update-perferences', views.UpdatePerferencesView.as_view(),name="update_perferences"),
    # path('<pk>/delete-products', views.ProductsDeleteView.as_view(),name="delete_products"),

]