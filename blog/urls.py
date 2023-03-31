from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home', views.homepage, name='homepage'),
    path('recipe/<int:id>', views.exploreRecipe, name='exploreRecipe'),
    path('categories', views.exploreCategories, name='exploreCategories'),
    path('categories/<str:id>', views.exploreCategoriesById, name='exploreCategoriesById'),
    path('search', views.searchRecipe, name='searchRecipe'),
    path('explore-latest', views.exploreLatest, name='exploreLatest'),
    path('explore-random', views.exploreRandom, name='exploreRandom'),
    path('submit-recipe', views.submit_recipe, name='submitRecipe'),
    # path('submit-recipe', views.submit_recipe_on_post, name='submitRecipeOnPost'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
]
