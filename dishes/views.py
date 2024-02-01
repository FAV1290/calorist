from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

from .models import Ingredient, Dish
from .documents import IngredientDocument, DishDocument



def index_view(request):
    return render(request, 'index.html')


def ingredients_view(request):
    all_ingredients = Ingredient.objects.all()
    ingredients_paginator = Paginator(all_ingredients, 15)
    page_number = request.GET.get('page', 1)
    adjusted_page = ingredients_paginator.get_page(page_number)
    return render(request, 'ingredients.html', {'ingredients_page': adjusted_page})


def dishes_view(request):
    all_dishes = Dish.objects.all()
    dishes_paginator = Paginator(all_dishes, 15)
    page_number = request.GET.get('page', 1)
    adjusted_page = dishes_paginator.get_page(page_number)
    return render(request, 'dishes.html', {'dishes_page': adjusted_page})


def search_view(request):
    query = request.GET.get('q', '')
    ingredients = [hit.name for hit in IngredientDocument.search().query('match', name=query)]
    dishes = [hit.name for hit in DishDocument.search().query('match', name=query)]
    return render(request, 'search.html', {'query': query, 'ingredients': ingredients, 'dishes': dishes})
