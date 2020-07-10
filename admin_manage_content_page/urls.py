
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageCustomPage.as_view(),name="custom_page"),
    path('add-page', views.CreatePageView.as_view(),name="add_page"),
    path('<pk>/update-page', views.PageUpdateView.as_view(),name="update_page"),
    path('<pk>/delete-page', views.PageDeleteView.as_view(),name="delete_page"),


]