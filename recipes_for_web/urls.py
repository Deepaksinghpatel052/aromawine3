from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.RecipesView.as_view(),name="revipe"),
    # # path('event-de', views.EventView.as_view(),name="event"),
    path('<int:pk>/quick-view-recipe', views.QuickViewRecipe.as_view(),name="quick_view_recipe"),
    path('detail/<slug:recipe_id>/<slug:recipe_slug>',  views.DetailView.as_view(),name="recipe_detail"),

]