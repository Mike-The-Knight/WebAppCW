from typing import Optional

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
def home(request):
    return render(request, 'website/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'website/about.html', {'title': 'About'})

# list users liked posts
def userLikes(request):
    return render(request, 'website/user_likes.html', {'title': 'Your liked posts'})

class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        already_liked = False
        for like in post.likes.all():
            if like == request.user:
                already_liked = True
                break
        if not already_liked:
            post.likes.add(request.user)

        if already_liked:
            post.likes.remove(request.user)


        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class AddComment(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        comment = Comment(author=request.user, post=post, text=request.POST['text'])
        comment.save()
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


## Class views for Posts
# List views
class PostListView(ListView):
    model = Post
    template_name = 'website/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


class UserPostListView(ListView):
    model = Post
    template_name = 'website/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        # get the user
        user = self.request.user
        # get the posts by that user
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        # call the base implementation to get a context
        context = super().get_context_data(**kwargs)
        # get post comments and add to context
        context["comments"] = Comment.objects.filter(post=self.object.id)
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/members/account/signin/'

    model = Post
    fields = ['title', 'type', 'description', 'ingredients', 'instructions']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = '/members/account/signin/'

    model = Post
    fields = ['title', 'description', 'ingredients', 'instructions']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = '/members/account/signin/'

    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

