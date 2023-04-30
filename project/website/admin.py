from django.contrib import admin
from .models import Meal, Recipe, Post, Like, Comment, Review

# Register your models here.
admin.site.register(Meal)
admin.site.register(Recipe)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Review)
