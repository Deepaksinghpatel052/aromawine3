from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageCategoryesView.as_view(),name="catogoryes"),
    path('add-categoryes', views.CreateCategoryView.as_view(),name="add_catogoryes"),
    path('<pk>/update-categoryes', views.CategoryUpdateView.as_view(),name="update_catogoryes"),
    path('<pk>/delete-categoryes', views.CategoryDeleteView.as_view(),name="delete_catogoryes"),

    # ===============  API START================================================================
    path('api/category', views.ApiCategoryView.as_view(),name="api_get_catogoryes"),
    # ===============  API END ================================================================


]
