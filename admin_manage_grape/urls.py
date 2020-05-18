from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageGrapeView.as_view(),name="grape"),
    path('add-grape', views.CreateGrapeView.as_view(),name="add_grape"),
    path('<pk>/update-grape', views.GrapeUpdateView.as_view(),name="update_grape"),
    path('<pk>/deoete-grape', views.GrapeDeleteView.as_view(),name="delete_grape"),

]