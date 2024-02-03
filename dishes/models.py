from django.db import models
from django.conf import settings

from django_resized import ResizedImageField


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
    name = models.CharField(
        max_length=128, null=False, blank=False, verbose_name='название ингредиента')
    kcal = models.FloatField(null=True, blank=True, verbose_name='ккал/100г')
    proteins = models.FloatField(null=True, blank=True, verbose_name='белки/100г')
    fats = models.FloatField(null=True, blank=True, verbose_name='жиры/100г')
    carbonhydrates = models.FloatField(null=True, blank=True, verbose_name='углеводы/100г')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        ordering = ['name']

    @property
    def nutrients_str(self) -> str:
        nutrients = [self.kcal, self.proteins, self.fats, self.carbonhydrates]
        nutrients_str = map(lambda x: f'{x:.2f}'.replace('.', ',') if x else '0,00', nutrients)
        return f'{" / ".join(nutrients_str)}'

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

    def __str__(self) -> str:
        return f'{self.ingredient.name} in {self.dish.name}'


class Dish(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False, verbose_name='название блюда')
    ingredients: models.ManyToManyField = models.ManyToManyField(
        Ingredient, through='DishIngredient')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    weight_cooked_grams = models.FloatField(
        null=False, blank=False, default=0, verbose_name='вес готового блюда (г)')

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'dishes'

    @property
    def weight_raw_grams(self) -> float:
        return sum(ingredient.weight_grams for ingredient in self.dishingredient_set.all())
    
    @property
    def cooking_loss_percentage(self) -> float:
        if self.weight_raw_grams:
            return (self.weight_raw_grams - self.weight_cooked_grams) * 100 / self.weight_raw_grams
        return 0
    
    @property
    def kcal(self) -> float:
        kcal_in_weight = sum(
            item.ingredient.kcal * item.weight_grams for item in self.dishingredient_set.all())
        cooking_loss_gain_coefficient = (self.cooking_loss_percentage / 100) + 1
        if self.weight_raw_grams:
            return kcal_in_weight / self.weight_raw_grams * cooking_loss_gain_coefficient
        return 0
    
    @property
    def proteins(self) -> float:
        proteins_in_weight = sum(
            item.ingredient.proteins * item.weight_grams for item in self.dishingredient_set.all())
        cooking_loss_gain_coefficient = (self.cooking_loss_percentage / 100) + 1
        if self.weight_raw_grams:
            return proteins_in_weight / self.weight_raw_grams * cooking_loss_gain_coefficient
        return 0
    
    @property
    def fats(self) -> float:
        fats_in_weight = sum(
            item.ingredient.fats * item.weight_grams for item in self.dishingredient_set.all())
        cooking_loss_gain_coefficient = (self.cooking_loss_percentage / 100) + 1
        if self.weight_raw_grams:
            return fats_in_weight / self.weight_raw_grams * cooking_loss_gain_coefficient
        return 0

    @property
    def carbonhydrates(self) -> float:
        carbonhydrates_in_weight = sum(
            item.ingredient.carbonhydrates * item.weight_grams for item in self.dishingredient_set.all())
        cooking_loss_gain_coefficient = (self.cooking_loss_percentage / 100) + 1
        if self.weight_raw_grams:
            return carbonhydrates_in_weight / self.weight_raw_grams * cooking_loss_gain_coefficient
        return 0

    def __str__(self) -> str:
        return self.name
 

class DishImage(models.Model):
    dish = models.OneToOneField(
        Dish, on_delete=models.CASCADE, primary_key=True, related_name='dish_image')
    image = ResizedImageField(
        size=[480, 270],
        crop=['middle', 'center'],
        upload_to='uploads/dishes_images',
        quality=75,
        force_format='PNG',
    )

    def __str__(self) -> str:
        return f'{self.dish.name} image'
