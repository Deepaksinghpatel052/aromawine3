from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageVarietalsView.as_view(),name="varietals"),
    # path('add-appellation', views.CreateAppellationView.as_view(),name="add_appellation"),
    path('<pk>/update-varietals', views.VarietalsUpdateView.as_view(),name="update_varietals"),
    path('<pk>/delete-varietals', views.VarietalsDeleteView.as_view(),name="delete_varietals"),


]
