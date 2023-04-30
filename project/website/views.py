from django.shortcuts import render
from .models import Meal, Recipe

# Create your views here.
def home(request):
    context = {
        'meals': Meal.objects.all(),
        'recipes': Recipe.objects.all(),
    }
    return render(request, "index.html", context)
