from typing import Optional
from django.shortcuts import render
from .models import Meal, Recipe
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def home(request):
    return render(request, 'website/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'website/about.html', {'title': 'About'})


# Class views for Meals and Recipes
class MealListView(ListView):
    model = Meal
    template_name = 'website/meals.html'
    context_object_name = 'meals'
    ordering = ['-date_posted']
    paginate_by = 2

class RecipeListView(ListView):
    model = Recipe
    template_name = 'website/recipes.html'
    context_object_name = 'recipes'
    ordering = ['-date_posted']
    paginate_by = 2

class MealDetailView(DetailView):
    model = Meal

class RecipeDetailView(DetailView):
    model = Recipe

class MealCreateView(LoginRequiredMixin, CreateView):
    login_url = '/members/account/signin'

    model = Meal
    fields = ['title', 'description', 'ingrediants']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeCreateView(LoginRequiredMixin, CreateView):
    login_url = '/members/account/signin/'

    model = Recipe
    fields = ['title', 'description', 'ingrediants', 'instructions']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class MealUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = '/members/account/signin'

    model = Meal
    fields = ['title', 'description', 'ingrediants']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = '/members/account/signin/'

    model = Recipe
    fields = ['title', 'description', 'ingrediants', 'instructions']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False

class MealDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Meal
    success_url = '/'

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = '/'

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False

