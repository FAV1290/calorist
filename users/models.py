from django.db import models
from django.contrib.auth.models import AbstractUser


class CaloristUser(AbstractUser):
    first_name = None
    last_name = None
    email = models.EmailField(unique=True, null=False, blank=False)
    date_updated = models.DateTimeField(auto_now=True, null=False)
    ingredients = models.ManyToManyField('dishes.Ingredient', through='dishes.UserIngredient')
    dishes = models.ManyToManyField('dishes.Dish', through='dishes.UserDish')

    class Meta:
        ordering = ['username']

    def get_full_name(self) -> str:
        return self.username

    def get_short_name(self) -> str:
        return self.username
