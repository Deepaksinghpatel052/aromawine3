from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageColorView.as_view(),name="color"),
    path('add-color', views.CreateColorView.as_view(),name="add_color"),
    path('<pk>/update-color', views.ColorUpdateView.as_view(),name="update_color"),
    path('<pk>/delete-color', views.ColorDeleteView.as_view(),name="delete_color"),


]