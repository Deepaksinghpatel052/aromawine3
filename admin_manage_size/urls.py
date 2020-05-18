from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageSizeView.as_view(),name="size"),
    # path('add-appellation', views.CreateAppellationView.as_view(),name="add_appellation"),
    path('<pk>/update-size', views.SizeUpdateView.as_view(),name="update_size"),
    path('<pk>/delete-size', views.SizeDeleteView.as_view(),name="delete_size"),


]
