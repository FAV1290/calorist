from django.urls import path

from .views import ingredients, index, search


urlpatterns = [
    path('', index, name='index'),
    path('ingredients/', ingredients, name='ingredients_all'),
    path('search/', search, name='search'),
]
