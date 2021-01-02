from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageProductsView.as_view(),name="products"),
    path('out-of-stock', views.OutOfStockView.as_view(),name="out_of_stock"),
    path('low-stock/', views.LowStockView.as_view(),name="low_stock"),
    path('<slug:prodict_id>/get-cost-and-stock', views.ManageProductCostView.as_view(),name="products_cost"),
    path('<slug:prodict_id>/get-product-all-wine', views.ManagProducFullImagtView.as_view(),name="products_all_image"),
    path('add-product', views.CreateProductView.as_view(),name="add_product"),
    path('<slug:prodict_id>/update-product', views.UpdateProductView.as_view(),name="update_products"),
    path('<pk>/delete-products', views.ProductsDeleteView.as_view(),name="delete_products"),
    path('get-product-vintage', views.get_product_vintage, name='get_product_vintage'),
    path('get-product-classifications', views.get_product_classifications, name='get_product_classifications'),
    path('add-new-producer', views.add_new_producer, name='add_new_producer'),
    path('select-appellation', views.select_appellation, name='select_appellation'),
    path('add-new-region', views.add_new_region, name='add_new_region'),
    path('check-lwin-code-in-database', views.CheckLwinCodeInDatabase, name='CheckLwinCodeInDatabase'),
    path('check-varietals-name', views.CkeckVarietalsName, name='CheckVarietalsName'),
    path('add-varietals-name', views.AddVarietalsName, name='AddVarietalsName'),
    path('check-appellation-name', views.CheckAppellationName, name='CheckAppellationName'),
    path('add-appellation-name', views.AddAppellationName, name='AddAppellationName'),

    path('check-flavours-name', views.CheckFlavoursName, name='CheckFlavoursName'),
    path('add-flavours-name', views.AddFlavoursName, name='AddFlavoursName'),

    path('check-classification-name', views.CheckClassificationName, name='CheckClassificationName'),
    path('add-classification-name', views.AddClassificationName, name='AddClassificationName'),

    path('check-food-pair-name', views.CheckfoodpairName, name='CheckfoodpairName'),
    path('add-foodpair-name', views.AddFoodpairName, name='AddFoodpairName'),

    path('add-product-info-by-ajax', views.AddProductInfoByAjax, name='AddProductInfoByAjax'),
    path('check-product-info-by-ajax', views.CheckProductInfoByAjax, name='CheckProductInfoByAjax'),

    path('<slug:id>/create-copy-of-product', views.CreateCopyOfProduct, name='CreateCopyOfProduct'),
]