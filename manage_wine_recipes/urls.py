from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ManageRecipesView.as_view(),name="recipes"),
    path('add-recipe', views.CreateRecipeView.as_view(),name="add_recipe"),
    path('<pk>/update-recipe', views.RecipeUpdateView.as_view(),name="update_recipe"),
    path('<pk>/delete-recipe', views.RecipeDeleteView.as_view(),name="delete_recipe"),


]