from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Ingredient
from .documents import IngredientDocument


def index(request):
    return render(request, 'index.html')


def ingredients(request):
    all_ingredients = Ingredient.objects.all()
    ingredients_paginator = Paginator(all_ingredients, 15)
    page_number = request.GET.get('page', 1)
    adjusted_page = ingredients_paginator.get_page(page_number)
    return render(request, 'ingredients.html', {'ingredients_page': adjusted_page})


def search(request):
    query = request.GET.get('q', '')
    search = IngredientDocument.search().query('match', name=query)
    results = [hit.name for hit in search]
    return render(request, 'search.html', {'results': results, 'query': query})
