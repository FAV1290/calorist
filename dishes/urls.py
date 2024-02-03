from django.urls import path

from .views import ingredients_view, dishes_view, index_view, search_view


urlpatterns = [
    path('', index_view, name='index'),
    path('ingredients/', ingredients_view, name='ingredients_all'),
    path('dishes/', dishes_view, name='dishes_all'),
    path('search/', search_view, name='search'),
]
