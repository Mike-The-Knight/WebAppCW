# REST API SERIALIZERS
from django.contrib.auth.models import User
from rest_framework import serializers
from members.serializers import UserSerializer
from .models import *


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'date_posted')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'author', 'text', 'date_posted', 'rating', 'title')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer()
    comments = CommentSerializer(many=True)
    likes = UserSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id',
                  'author',
                  'title',
                  'date_posted',
                  'type',
                  'description',
                  'instructions',
                  'ingredients',
                  'likes',
                  'comments',
                  'reviews'
                  )
