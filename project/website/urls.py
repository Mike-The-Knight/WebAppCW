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
from .views import AddLike, AddComment, AddReview

urlpatterns = [
    # paths for home page and about page
    path('', views.PostListView.as_view(), name="home"),
    path('about', views.about, name="about"),

    # Paths for viewing, updating, creating and deleting posts
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),
    path('post/create/', views.PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name="post-delete"),

    # Paths for viewing posts by a specific user
    path('user/<str:username>/', views.UserPostListView.as_view(), name="user-posts"),

    # View all posts liked by a user
    path('likes', views.user_likes, name="user-likes"),

    # View all posts by the users the user follows
    path('following', views.user_following, name="user-following"),

    # View all posts by the users the user follows
    path('posts', views.createpost, name="post_form"),

    # View all posts by a particular user using their id
    path('post/user/<int:pk>', views.user_posts_id, name="user-posts-id"),

    # like/unlike post
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),

    # post new comments
    path('post/<int:pk>/comment', AddComment.as_view(), name='comment'),

    # post new reviews
    path('post/<int:pk>/review', AddReview.as_view(), name='review')
]
