from django.shortcuts import render
from .models import Meal, Recipe
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
def home(request):
    context = {
        'meals': Meal.objects.all(),
        'recipes': Recipe.objects.all(),
    }
    return render(request, 'website/home.html', context)

def about(request):
    return render(request, 'website/about.html', {'title': 'About'})

# Class views for Meals and Recipes
class MealListView(ListView):
    model = Meal
    template_name = 'website/home.html'
    context_object_name = 'meals'
    ordering = ['-date_posted']

class RecipeListView(ListView):
    model = Recipe
    template_name = 'website/home.html'
    context_object_name = 'recipes'
    ordering = ['-date_posted']

class MealDetailView(DetailView):
    model = Meal

class RecipeDetailView(DetailView):
    model = Recipe

class MealCreateView(CreateView):
    model = Meal
    fields = ['title', 'content']

class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['title', 'content']

class MealUpdateView(UpdateView):
    model = Meal
    fields = ['title', 'content']

class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['title', 'content']

class MealDeleteView(DeleteView):
    model = Meal
    success_url = '/'

class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = '/'

