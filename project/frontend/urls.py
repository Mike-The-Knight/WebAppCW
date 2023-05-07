from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('home', index),
    path('about', index),
    path('signin', index),
    path('signup', index),
    path('post/<int:pk>/', index)
]