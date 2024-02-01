from django.core.paginator import Paginator
from django.contrib.auth import logout, get_user_model
from django.shortcuts import HttpResponseRedirect, render


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def user_ingredients_view(request, username):
    user_ingredients = get_user_model().objects.get(username=username).ingredients.all()
    ingredients_paginator = Paginator(user_ingredients, 15)
    page_number = request.GET.get('page', 1)
    adjusted_page = ingredients_paginator.get_page(page_number)
    return render(request, 'ingredients.html', {'ingredients_page': adjusted_page})


def user_dishes_view(request, username):
    user_dishes = get_user_model().objects.get(username=username).dishes.all()
    dishes_paginator = Paginator(user_dishes, 15)
    page_number = request.GET.get('page', 1)
    adjusted_page = dishes_paginator.get_page(page_number)
    return render(request, 'dishes.html', {'dishes_page': adjusted_page})
