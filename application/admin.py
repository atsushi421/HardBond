from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.User)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Obon)
class CategoryAdmin(admin.ModelAdmin):
    pass