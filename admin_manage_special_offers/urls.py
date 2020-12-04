from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ManageSpecialOffer.as_view(), name="special_offer"),
    path('add-offers', views.CreateSpecialOffereView.as_view(), name="add_offers"),
    path('<pk>/update-offer', views.OfferUpdateView.as_view(), name="update_offer"),
    path('<pk>/delete-offer', views.OfferDeleteView.as_view(), name="delete_orrer"),

]