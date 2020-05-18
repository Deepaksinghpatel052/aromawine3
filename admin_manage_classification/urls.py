from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageClassificationView.as_view(),name="classification"),
    # path('add-appellation', views.CreateAppellationView.as_view(),name="add_appellation"),
    path('<pk>/update-classification', views.ClassificationUpdateView.as_view(),name="update_classification"),
    path('<pk>/delete-classification', views.ClassificationDeleteView.as_view(),name="delete_classification"),


]
