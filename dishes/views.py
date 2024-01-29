from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def ingredients(request):
    return render(request, 'ingredients.html')
