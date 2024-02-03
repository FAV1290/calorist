from django.forms import ModelForm

from .models import Ingredient


class IngredientAddForm(ModelForm):
    class Meta:
        model = Ingredient
        exclude = ['created_by']
