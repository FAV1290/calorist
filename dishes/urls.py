from django.urls import path

from .views import (
    index_view, search_view,
    dish_view, dishes_view, 
    ingredients_view, ingredient_add_view,
    add_dish_to_profile_view, delete_dish_from_profile_view, 
    add_ingredient_to_profile_view, delete_ingredient_from_profile_view,
)


urlpatterns = [
    path('', index_view, name='index'),
    path('dish/<int:id>/', dish_view, name='dish'),
    path('dishes/', dishes_view, name='dishes_all'),
    path('dishes/add_to_profile/', add_dish_to_profile_view, name='own_dish'),
    path('dishes/delete_from_profile/', delete_dish_from_profile_view, name='release_dish'),
    path('ingredients/', ingredients_view, name='ingredients_all'),
    path('ingredients/add/', ingredient_add_view, name='add_ingredient'),
    path('ingredients/add_to_profile/', add_ingredient_to_profile_view, name='own_ingredient'),
    path(
        'ingredients/delete_from_profile/',
        delete_ingredient_from_profile_view,
        name='release_ingredient'
    ),
    path('search/', search_view, name='search'),
]
