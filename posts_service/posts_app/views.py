from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .models import *


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("date_posted")
    serializer_class = PostSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all().order_by("user")
    serializer_class = LikeSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("date_posted")
    serializer_class = CommentSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by("date_posted")
    serializer_class = ReviewSerializer
