from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageAppellationView.as_view(),name="appellation"),
    # path('add-appellation', views.CreateAppellationView.as_view(),name="add_appellation"),
    path('<pk>/update-appellation', views.appellationUpdateView.as_view(),name="update_appellation"),
    path('<pk>/delete-appellation', views.AppellationDeleteView.as_view(),name="delete_appellation"),


]
