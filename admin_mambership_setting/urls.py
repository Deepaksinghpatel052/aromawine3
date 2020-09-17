from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ManageMembershipView.as_view(), name="membership"),
    path('<pk>/update-membership', views.ManageUpdateView.as_view(),name="update_membership"),
    path('<pk>/delete-membership', views.MembershipDeleteView.as_view(),name="delete_membership"),

   
]