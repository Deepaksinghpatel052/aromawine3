from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageVintagesView.as_view(),name="vintages"),
    # path('add-appellation', views.CreateAppellationView.as_view(),name="add_appellation"),
    path('<pk>/update-vintages', views.VintagesUpdateView.as_view(),name="update_vintages"),
    path('<pk>/delete-vintages', views.VintagesDeleteView.as_view(),name="delete_vintages"),


]
