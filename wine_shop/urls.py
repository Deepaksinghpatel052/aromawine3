from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowView.as_view(),name="wine_shop"),
    path('filters', views.product_list,name="wine_shop_filter"),
    path('<int:pk>/quick-view-product', views.QuickVuewProduct.as_view(),name="quick_view_product"),
]