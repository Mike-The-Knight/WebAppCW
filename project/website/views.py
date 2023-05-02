from typing import Optional

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LikeForm
from .models import Post, Like, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def home(request):
    return render(request, 'website/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'website/about.html', {'title': 'About'})

def like(request):
    if request.method == "POST":
        form = LikeForm(request.POST)
        if form.is_valid():
            # add like to DB
            userid = form.cleaned_data["userid"]
            postid = form.cleaned_data["postid"]
            user = User.objects.get(id=userid)
            post = Post.objects.get(id=postid)
            new_like = Like(user=user, post=post)
            new_like.save()
            return HttpResponseRedirect('/post/' + str(postid))
    return HttpResponseRedirect('/')

def unlike(request):
    if request.method == "POST":
        form = LikeForm(request.POST)
        if form.is_valid():
            # find like and remove from DB
            userid = form.cleaned_data["userid"]
            postid = form.cleaned_data["postid"]
            user = User.objects.get(id=userid)
            post = Post.objects.get(id=postid)
            like_to_delete = Like.objects.filter(post=post).filter(user=user)
            like_to_delete.delete()
            return HttpResponseRedirect('/post/' + str(postid))
    return HttpResponseRedirect('/')

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
        # get post likes and add to context
        context["likes"] = Like.objects.filter(post=self.object.id)
        if((Like.objects.filter(post=self.object.id)).filter(user=self.request.user.id)):
            context["liked"] = True
        else:
            context["liked"] = False

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

