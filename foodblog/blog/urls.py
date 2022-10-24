from django.urls import path
from . import views
from .views import RecipeListView, RecipeDetailView, CreateRecipe, UpadateRecipe
urlpatterns = [
    # path('',views.Blog),
    path('recipes',RecipeListView.as_view(),name='recipes'),
    path('recipes/<int:pk>',RecipeDetailView.as_view(),name='recipe_det'),
    path('stories',views.stories_list,name='stories'),
    path('like-recipe/<int:id>',views.like_recipe,name='like_recipe'),
    
    path('recipes/create',CreateRecipe.as_view(),name='create_recipe'),
    path('recipes/update/<int:pk>',UpadateRecipe.as_view(),name='update_recipe'),
    # path('stories/create',CreateRecipe.as_view(),name='create_recipe'),
    
    
    
    
]
