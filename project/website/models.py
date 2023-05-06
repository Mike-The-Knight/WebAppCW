from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


#  Comments only have a text field
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(default=timezone.now)
    text = models.TextField()

    def __str__(self):
        return self.text


#  Reviews have a title, text and a rating 0-5
class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(default=timezone.now)
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
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    comments = models.ManyToManyField(Comment, blank=True, related_name='comments')
    reviews = models.ManyToManyField(Review, blank=True, related_name='reviews')

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
        return reverse('post-detail', kwargs={'pk': self.pk})




