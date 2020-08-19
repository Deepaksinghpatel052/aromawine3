from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageEventView.as_view(),name="event"),
    path('add-event', views.CreateEventView.as_view(),name="add_event"),
    path('<pk>/update-event', views.EventUpdateView.as_view(),name="update_event"),
    path('<pk>/delete-event', views.EventDeleteView.as_view(),name="delete_event"),


]