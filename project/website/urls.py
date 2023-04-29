"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    # paths for home page and about page
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    # paths for viewing meals and recipes
    path('meals', views.MealListView.as_view(), name="meals"),
    path('recipes', views.RecipeListView.as_view(), name="recipes"),
    path('meal/<int:pk>/', views.MealDetailView.as_view(), name="meal-detail"),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name="recipe-detail"),
    # paths for creating and deleting meals and recipes
    path('meal/create/', views.MealCreate.as_view(), name="meal-create"),
    path('meal/<int:pk>/delete/', views.MealDelete.as_view(), name="meal-delete"),
    path('recipe/create/', views.RecipeCreate.as_view(), name="recipe-create"),
    path('recipe/<int:pk>/delete/', views.RecipeDelete.as_view(), name="recipe-delete"),
    # paths for updating meals and recipes
    path('meal/<int:pk>/update/', views.MealUpdate.as_view(), name="meal-update"),
    path('recipe/<int:pk>/update/', views.RecipeUpdate.as_view(), name="recipe-update"),    
]
