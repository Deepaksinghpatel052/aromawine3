from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageBannersView.as_view(),name="banners"),
    path('add-banner', views.CreateBannerView.as_view(),name="add_banners"),
    path('<pk>/update-banners', views.BannersUpdateView.as_view(),name="update_banners"),
    path('<pk>/delete-banners', views.BannersDeleteView.as_view(),name="delete_banners"),


]
