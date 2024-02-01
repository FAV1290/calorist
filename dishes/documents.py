from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from .models import Ingredient, Dish


@registry.register_document
class IngredientDocument(Document):
    class Index:
        name = 'ingredients'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Ingredient
        fields = ['name']


@registry.register_document
class DishDocument(Document):
    class Index:
        name = 'dishes'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Dish
        fields = ['name']
