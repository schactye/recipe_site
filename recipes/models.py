from django.db import models

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('breakfast', 'Завтрак'),
        ('lunch', 'Обед'),
        ('dinner', 'Ужин'),
    ]
    
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='breakfast')

    def __str__(self):
        return self.title