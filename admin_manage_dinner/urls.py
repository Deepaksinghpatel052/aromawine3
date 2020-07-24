from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageDinnerView.as_view(),name="dinner"),
    path('add-dinner', views.CreateDinnerView.as_view(), name="add_dinner"),
    path('<pk>/update-dinner', views.DinnerUpdateView.as_view(), name="update_dinner"),
    path('<pk>/deoete-dinner', views.DinnerDeleteView.as_view(), name="delete_dinner"),

]