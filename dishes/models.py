from django.db import models

from django.conf import settings


class UserIngredient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)

    class Meta:
        ordering = ['ingredient', 'user']

    def __str__(self) -> str:
        return f'{self.ingredient.name} by {self.user.username}'


class UserDish(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)

    class Meta:
        ordering = ['dish', 'user']
        verbose_name_plural = 'User dishes'

    def __str__(self) -> str:
        return f'{self.dish.name} by {self.user.username}'


class Ingredient(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    kcal = models.FloatField(null=True, blank=True)
    proteins = models.FloatField(null=True, blank=True)
    fats = models.FloatField(null=True, blank=True)
    carbonhydrates = models.FloatField(null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        nutrients = [self.kcal, self.proteins, self.fats, self.carbonhydrates]
        nutrients_str = map(lambda x: f'{x:.2f}'.replace('.', ',') if x else '-', nutrients)
        nutrients_str = map(''.join, zip(['К: ', 'Б: ', 'Ж: ', 'У: '], nutrients_str))
        return f'{self.name} ({" / ".join(nutrients_str)})'


class DishIngredient(models.Model):
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    weight_grams = models.FloatField(null=False, blank=False)

    class Meta:
        ordering = ['ingredient', 'dish']


class Dish(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    ingredients: models.ManyToManyField = models.ManyToManyField(Ingredient, through='DishIngredient')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'dishes'

    def __str__(self) -> str:
        return self.name
