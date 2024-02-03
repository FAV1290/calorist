from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Ingredient, Dish
from .documents import IngredientDocument, DishDocument
from .forms import IngredientAddForm


def index_view(request):
    return render(request, 'index.html')


def ingredients_view(request):
    all_ingredients = Ingredient.objects.all().order_by('-created_at')
    ingredients_paginator = Paginator(all_ingredients, 15)
    page_number = request.GET.get('page', 1)
    adjusted_page = ingredients_paginator.get_page(page_number)
    return render(request, 'ingredients.html', {'ingredients_page': adjusted_page})


def add_ingredient_to_profile_view(request):
    if request.POST.get('own_ingredient_id'):
        request.user.ingredients.add(Ingredient.objects.get(pk=request.POST.get('own_ingredient_id')))
    return redirect(request.META.get('HTTP_REFERER', 'index'))


def delete_ingredient_from_profile_view(request):
    if request.POST.get('release_ingredient_id'):
        request.user.ingredients.remove(Ingredient.objects.get(pk=request.POST.get('release_ingredient_id')))
    return redirect(request.META.get('HTTP_REFERER', 'index'))


def add_dish_to_profile_view(request):
    if request.POST.get('own_dish_id'):
        request.user.dishes.add(Dish.objects.get(pk=request.POST.get('own_dish_id')))
    return redirect(request.META.get('HTTP_REFERER', 'index'))


def delete_dish_from_profile_view(request):
    if request.POST.get('release_dish_id'):
        request.user.dishes.remove(Dish.objects.get(pk=request.POST.get('release_dish_id')))
    return redirect(request.META.get('HTTP_REFERER', 'index'))

def dishes_view(request):
    all_dishes = Dish.objects.all().prefetch_related('dish_image')
    dishes_paginator = Paginator(all_dishes, 5)
    page_number = request.GET.get('page', 1)
    adjusted_page = dishes_paginator.get_page(page_number)
    return render(request, 'dishes.html', {'dishes_page': adjusted_page})


def dish_view(request, id):
    target_dish = Dish.objects.get(pk=id)
    image = target_dish.dish_image.image.url if getattr(target_dish, 'dish_image', None) else None
    return render(
        request, 'dish.html', 
        {
            'dish': target_dish,
            'dish_image_url': image,
            'dish_ingredients': target_dish.dishingredient_set.all(),
        }
    )


def search_view(request):
    query = request.GET.get('q', '')
    found_ingredients_ids = [hit.meta.id for hit in IngredientDocument.search().query('match', name=query)]
    found_dishes_ids = [hit.meta.id for hit in DishDocument.search().query('match', name=query)]
    found_ingredients = Ingredient.objects.filter(pk__in=found_ingredients_ids)
    found_dishes = Dish.objects.filter(pk__in=found_dishes_ids)
    return render(request, 'search.html', {'query': query, 'ingredients': found_ingredients, 'dishes': found_dishes})


def ingredient_add_view(request):
    if request.method == 'POST':
        new_ingredient = Ingredient(created_by=request.user)
        form = IngredientAddForm(request.POST, instance=new_ingredient)
        if form.is_valid():
            form.save()
        return redirect('ingredients_all')
    else:
        form = IngredientAddForm()
        return render(request, 'add.html', {'form': form, 'form_action': 'add_ingredient'})
