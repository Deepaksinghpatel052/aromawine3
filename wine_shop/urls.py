from django.urls import path
from . import views


urlpatterns = [
    path('', views.ShowView.as_view(),name="wine_shop"),
    path('filters', views.product_list,name="wine_shop_filter"),
    path('<int:pk>/quick-view-product', views.QuickVuewProduct.as_view(),name="quick_view_product"),


    path('wine-full-view', views.WineFullView.as_view(),name="wine_full_view"),
    # ===============  API START================================================================
    path('api/wine-according-to-category', views.ApiWineByCategory.as_view(), name="api_wine_by_category"),
    path('api/one-wine-by-id', views.ApiOneWineById.as_view(), name="one_wine_by_id"),
    path('api/all-image-of-one-product', views.ApiAllImageOfOneProduct.as_view(), name="ApiAllImageOfOneProduct"),


    # ===============  API END ================================================================
]