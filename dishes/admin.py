from django.contrib import admin

from dishes.models import Ingredient, DishIngredient, Dish, UserIngredient, UserDish


@admin.register(Dish, Ingredient, DishIngredient, UserIngredient, UserDish)
class DishesAdmin(admin.ModelAdmin):
    pass
