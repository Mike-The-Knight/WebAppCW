from django.contrib import admin
from .models import Post, Like, Comment, Review

# Register your models here.
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Review)
