from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddressBookList.as_view(),name="addressbooklist"),
    path('add-new-address', views.AddNewAddress.as_view(),name="add_new_address"),
    path('<pk>/update-address', views.AddressUpdateView.as_view(),name="update_address"),
    path('<pk>/remove-address', views.RemoveAddress,name="RemoveAddress"),
]