from django.db import models


class ProfileStatus(models.IntegerChoices):
    DELETED = 1
    BANNED = 2
    ACTIVE = 3
