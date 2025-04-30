from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'category', 'image']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название рецепта'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание',
                'rows': 3
            }),
            'ingredients': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ингредиенты (по одному в строке)',
                'rows': 5
            }),
            'instructions': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Пошаговые инструкции',
                'rows': 8
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
        
        labels = {
            'title': 'Название рецепта',
            'description': 'Описание',
            'ingredients': 'Ингредиенты',
            'instructions': 'Инструкции по приготовлению',
            'category': 'Категория',
            'image': 'Изображение блюда'
        }