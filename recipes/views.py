from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'recipes/home.html')

def breakfast(request):
    recipes = Recipe.objects.filter(category='Завтрак')
    return render(request, 'recipes/breakfast.html', {'recipes': recipes, 'category': 'Завтраки'})

def lunch(request):
    recipes = Recipe.objects.filter(category='Обед')
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes, 'category': 'Обеды'})

def dinner_recipes(request):
    recipes = Recipe.objects.filter(category='Ужин')
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes, 'category': 'Ужины'})

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                new_recipe = form.save()
                # Используем стандартный messages framework
                request._messages.add_message(
                    request._messages.INFO,
                    f'Рецепт "{new_recipe.title}" успешно добавлен!'
                )
                return redirect('recipes:home')
            except Exception as e:
                # Логируем ошибку в консоль
                print(f"Ошибка сохранения: {e}")
                # Альтернативный способ показать ошибку
                form.errors['__all__'] = form.error_class([
                    'Произошла ошибка при сохранении рецепта'
                ])
        # Если форма не валидна, ошибки уже есть в form.errors
    else:
        form = RecipeForm()
    
    return render(request, 'recipes/add_recipe.html', {
        'form': form,
        'title': 'Добавить рецепт'
    })