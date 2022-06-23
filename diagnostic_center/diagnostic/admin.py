from django.contrib import admin
from . import models


@admin.register(models.Test)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
