from django.urls import path

from .generic_views import RecipeApiView,CatagoryApiView, RecipeReadUpdateDeleteView


urlpatterns = [
    path('recipes/',RecipeApiView.as_view(),name='recipes_api'),
    path('recipes/<int:pk>/',RecipeReadUpdateDeleteView.as_view(),name='recipe_api'),
    path('catagories/',CatagoryApiView.as_view(),name='catagories_api'),

]
