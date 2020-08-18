from django.db import models

# Create your models here.
class Ingredient(models.Model):
    MEASURE_CHOICES = (
        ('L', 'Liter'),
        ('G', 'Gram')
    )
    CURRENCY_CHOICES = (
        ('USD', 'US Dollars'),
        ('EUR', 'EURO'),
        ('BRL', 'BRAZILIAN REAL')
    )
    name = models.CharField(max_length=250)
    article_number = models.CharField(max_length=250) #See bar code pattern
    measure = models.DecimalField(max_digits=19, decimal_places=3)
    unit_of_measure = models.CharField(max_length=1, choices=MEASURE_CHOICES)
    measure_scale = models.IntegerField()
    cost = models.DecimalField(max_digits = 19, decimal_places=3)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)


class Recipe(models.Model):
    name = models.CharField(max_length=250)
    
    

class RecipeIngredientQuantity(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits = 19, decimal_places=3)
    scale = models.IntegerField()

    class Meta:
        unique_together = ('recipe', 'ingredient')