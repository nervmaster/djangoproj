from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello, world!')

def list_recipe(request):
    return HttpResponse('All recipes')

def list_ingredient(request):
    return HttpResponse('List all ingredients')

def create_recipe(request):
    return HttpResponse('You are creating a recipe!')

def create_ingredient(request):
    return HttpResponse('You are creating an ingredient!')

def manage_recipe(request, recipe_id):
    return HttpResponse('You are editing recipe {}'.format(recipe_id))

def manage_ingredient(request, ingredient_id):
    return HttpResponse('You are editing ingredient {}'.format(ingredient_id))