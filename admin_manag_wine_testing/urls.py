from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageTestingView.as_view(),name="testing_wine"),
    path('add-testing-wine', views.CreateTestingView.as_view(), name="add_testing"),
    path('<pk>/update-testing-wine', views.TestingUpdateView.as_view(), name="update_testing"),
    path('<pk>/deoete-testing-wine', views.TestingDeleteView.as_view(), name="delete_testing"),

]