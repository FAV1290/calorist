from django.contrib import admin

from dishes.models import Ingredient, DishIngredient, Dish, UserIngredient, UserDish, DishImage


@admin.register(Dish, Ingredient, DishIngredient, UserIngredient, UserDish, DishImage)
class DishesAdmin(admin.ModelAdmin):
    pass
