from django.urls import path
from . import views


urlpatterns = [
    path('<slug:type>/<slug:page_slug>/', views.PageContentView.as_view(),name="page"),
]