from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Ingredient


def index(request):
    return render(request, 'index.html')


def ingredients(request):
    all_ingredients = Ingredient.objects.all()
    ingredients_paginator = Paginator(all_ingredients, 20)
    page_number = request.GET.get('page')
    adjusted_page = ingredients_paginator.get_page(page_number)
    return render(request, 'ingredients.html', {'ingredients_page': adjusted_page})
