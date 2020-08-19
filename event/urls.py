from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.EventView.as_view(),name="event"),
    # path('event-de', views.EventView.as_view(),name="event"),
    path('<int:pk>/quick-view-event', views.QuickVuewEvent.as_view(),name="quick_view_event"),
    path('detail/<slug:event_id>/<slug:event_slug>',  views.DetailView.as_view(),name="event_detail"),

]