from django.contrib import admin

from users.models import CaloristUser


@admin.register(CaloristUser)
class CaloristUserAdmin(admin.ModelAdmin):
    pass
