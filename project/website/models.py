from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Meal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    ingrediants = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('meal-detail', kwargs={'pk': self.pk})


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    ingrediants = models.TextField()
    instructions = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})
    

class Post(models.Model):

    # 2 post types
    TYPE_CHOICES = (
        ("RECIPE", 'Recipe'),
        ("MEAL", 'Meal')
    )

    title = models.CharField(max_length=150)
    type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES
    )
    date_posted = models.DateField(default=timezone.now)
    description = models.TextField()
    ingredients = models.TextField(blank=True)  # only 'recipe' posts will have this
    instructions = models.TextField(blank=True)  # only 'recipe' posts will have this


    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def all_fields(self):
        output = "Title: " + self.title
        output += ", Type: " + self.type
        output += ", Date posted: " + str(self.date_posted)
        output += ", Description: " + self.description
        output += ", Ingredients: " + self.ingredients
        output += ", Instructions: " + self.instructions
        output += ", Author: " + self.author.username
        return output

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})

#  Users can 'like' posts
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " LIKES " + self.post.title

#  Comments only have a text field
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_posted = models.DateField()
    text = models.TextField()

    def __str__(self):
        return self.text

#  Reviews have a title, text and a rating 0-5
class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_posted = models.DateField()
    title = models.CharField(max_length=150)
    text = models.TextField()
    rating = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.title