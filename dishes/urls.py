from django.urls import path

from .views import ingredients, index


urlpatterns = [
    path('', index, name='index'),
    path('ingredients/', ingredients, name='ingredients_all'),
]
