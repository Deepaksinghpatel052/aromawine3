from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageFlavoursView.as_view(),name="flavours"),
    path('<pk>/update-flavours', views.FlavoursUpdateView.as_view(),name="update_flavours"),
    path('<pk>/delete-flavours', views.FlavoursDeleteView.as_view(),name="delete_flavours"),


]