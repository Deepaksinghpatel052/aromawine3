from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageProducerView.as_view(),name="producer"),
    path('add-producer', views.CreateProducerView.as_view(),name="add_producer"),
    path('<pk>/update-producer', views.ProducerUpdateView.as_view(),name="update_producer"),
    path('<pk>/deoete-producer', views.GeeksDeleteView.as_view(),name="delete_producer"),

]
