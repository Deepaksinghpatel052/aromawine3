from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ManageGeneralSettingView.as_view(), name="general"),
    # path('add-grape', views.CreateGrapeView.as_view(), name="add_grape"),
    path('<pk>/update-grape', views.GeneralUpdateView.as_view(), name="update_general"),
    path('<pk>/delete-shipping', views.ShippingDeleteView.as_view(), name="delete_shipping"),
    path('fee-shipping', views.ManageShippingSettingView.as_view(), name="shipping"),
    path('fee-shipping-update', views.update_shipping, name="shipping_update"),


    # ===============  API START================================================================
    path('api/wine-project-info', views.ApiWineProjectInfo.as_view(), name="api_wine_project_info"),
    # ===============  API END ================================================================

]