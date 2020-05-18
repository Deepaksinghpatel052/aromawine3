from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageRegionView.as_view(),name="region"),
    path('add-region', views.CreateRegionView.as_view(),name="add_region"),
    path('<pk>/update-region', views.RegionUpdateView.as_view(),name="update_region"),
    path('<pk>/deoete-region', views.RegionDeleteView.as_view(),name="delete_region"),

]