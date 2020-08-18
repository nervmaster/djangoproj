from django.db import models
from decimal import Decimal

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
    measure_scale_factor = models.DecimalField(max_digits=12, decimal_places=6)
    cost = models.DecimalField(max_digits = 19, decimal_places=3)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

    def __str__(self):
        output = 'name: {} ({}) '.format(self.name, self.id)
        output += 'article_number: {} '.format(self.article_number)
        output += 'measure: {} '.format(self.measure)
        output += 'unit_of_measure: {} '.format(self.unit_of_measure)
        output += 'measure_scale_factor: {} '.format(self.measure_scale_factor)
        output += 'cost: {} '.format(self.measure_scale_factor)
        output += 'currency: {} '.format(self.currency)

        return output

    def  get_base_cost(self):
        return self.cost / (self.measure * self.measure_scale_factor)


class Recipe(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return 'name: {} ({})'.format(self.name, self.id)
    

class RecipeIngredientQuantity(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits = 19, decimal_places=3)
    scale_factor = models.DecimalField(max_digits=12, decimal_places=6)

    class Meta:
        unique_together = ('recipe', 'ingredient')
    
    def __str__(self):
        output = 'recipe: {} ({}) '.format(self.recipe.name, self.recipe.id)
        output += 'ingredient: {} ({}) '.format(self.ingredient.name, self.ingredient.id)
        output += 'quantity: {} '.format(self.quantity)
        output += 'scale_factor: {}'.format(self.scale_factor)
        return output

    def get_ingredient_cost(self):
        return self.quantity * self.ingredient.get_base_cost() * self.scale_factor