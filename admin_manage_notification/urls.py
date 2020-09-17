from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ManageNotificationView.as_view(), name="notification"),
    path('<pk>/update-notification', views.ManageUpdateView.as_view(),name="update_notification"),
    path('<pk>/send-notification', views.send_notification,name="send_notification"),
    path('<pk>/delete-notification', views.NotificationDeleteView.as_view(),name="delete_notification"),
]