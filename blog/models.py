from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'img')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    email = models.EmailField(null=True)
    ingredients = models.TextField(null=True)
    CATEGORY_CHOICES = [
        ('Thai', 'Thai'),
        ('American', 'American'),
        ('Chinese', 'Chinese'),
        ('Mexican', 'Mexican'),
        ('Indian', 'Indian'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Indian')
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)

    def get_ingredients_list(self):
        return self.ingredients.split(",")

    def __str__(self):
        return self.name


