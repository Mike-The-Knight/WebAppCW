from django.contrib import admin
from .models import Meal, Recipe

# Register your models here.
admin.site.register(Meal)
admin.site.register(Recipe)