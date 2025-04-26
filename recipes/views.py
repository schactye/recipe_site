from django.shortcuts import render
from .models import Recipe

def home(request):
    return render(request, 'recipes/home.html')

def breakfast_list(request):
    recipes = Recipe.objects.filter(category='breakfast')
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes, 'category': 'Завтраки'})

def lunch_list(request):
    recipes = Recipe.objects.filter(category='lunch')
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes, 'category': 'Обеды'})

def dinner_list(request):
    recipes = Recipe.objects.filter(category='dinner')
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes, 'category': 'Ужины'})