from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(),name="home"),
    path('product_image/<slug:product_id>', views.get_product_image_one_by_product_id,name="get_product_image_one_by_product_id"),
    path('page/<slug:title>', views.CustomPageView.as_view(),name="custom_page"),

    #==================================API========================
    path('api/banner', views.ApiGetBannerView.as_view(),name="api_banner"),
    path('api/tranding-wines', views.ApiTrandingWineView.as_view(),name="api_tranding_wine"),
    #==================================API========================
]