from django.urls import path
from . import views

urlpatterns = [
    path('', views.PaymentMethod.as_view(),name="payment_method"),
    path('<pk>/remove-payment', views.RemovePayment, name="RemovePayment"),
    # path('add-new-card', views.AddNewPayment.as_view(),name="add_new_payment"),
    # path('<pk>/update-address', views.AddressUpdateView.as_view(),name="update_address"),
    # path('<pk>/remove-address', views.RemoveAddress,name="RemoveAddress"),
]