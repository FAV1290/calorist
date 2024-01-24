from django.db import models

from calorist.settings import AUTH_USER_MODEL


class UserIngredient(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)

    class Meta:
        ordering = ['ingredient', 'user']

class UserDish(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)

    class Meta:
        ordering = ['dish', 'user']

class Ingredient(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    kcal = models.FloatField(null=True, blank=True)
    proteins = models.FloatField(null=True, blank=True)
    fats = models.FloatField(null=True, blank=True)
    carbonhydrates = models.FloatField(null=True, blank=True)
    created_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        nutrients = [self.kcal, self.proteins, self.fats, self.carbonhydrates]
        nutrients_str = map(lambda x: f'{x:.2f}' if x else '-', nutrients)
        return f'{self.name} ({"/".join(nutrients_str)})'


class DishIngredient(models.Model):
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    weight_grams = models.FloatField(null=False, blank=False)

    class Meta:
        ordering = ['ingredient', 'dish']


class Dish(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    ingredients = models.ManyToManyField(Ingredient, through='DishIngredient')
    created_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        ordering = ['name']
