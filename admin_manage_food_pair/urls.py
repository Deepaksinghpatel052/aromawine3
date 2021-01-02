from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageFoodPairView.as_view(),name="foodpair"),
    path('<pk>/update-foodpair', views.foodpairUpdateView.as_view(),name="update_foodpair"),
    path('<pk>/delete-foodpair', views.FoodpairDeleteView.as_view(),name="delete_foodpair"),


]