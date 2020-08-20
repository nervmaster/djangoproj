from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/<int:recipe_id>', views.manage_recipe, name='manage recipe'),
    path('recipe/new', views.create_recipe, name='create recipe'),
    path('recipe/', views.list_recipe, name='all recipes'),
    path('ingredient/<int:ingredient_id>', views.manage_ingredient, name='manage ingredient'),
    path('ingredient/new', views.create_ingredient, name='create ingredient'),
    path('ingredient/', views.list_ingredient, name='all ingredient')
]