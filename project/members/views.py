from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views import View

# Create your views here.
def account(request):
    return render(request, 'members/profile.html', {'title': 'Account'})

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('signin')
    else:
        form = UserRegisterForm()
    return render(request, 'members/signup.html', {'form': form})


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in Successfully!")
            return redirect("home")
        else:
            messages.error(request, "Incorrect username or password")
            return redirect("signin")

    else:
        return render(request, 'members/signin.html', {'title': 'Sign in'})

def signout(request):
    logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect("home")

@login_required
def update_account(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('account')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'members/profile_update.html', context)

class Follow(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        user_to_follow = User.objects.get(pk=pk)
        already_following = False

        for followed_user in request.user.profile.following.all():
            if followed_user == user_to_follow:
                already_following = True
                break

        if not already_following:
            request.user.profile.following.add(user_to_follow)
            user_to_follow.profile.followers.add(request.user)


        if already_following:
            request.user.profile.following.remove(user_to_follow)
            user_to_follow.profile.followers.remove(request.user)


        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


def view_user(request, pk):
    viewed_user = User.objects.get(pk=pk)
    return render(request, 'members/user_detail.html', { 'title': 'View user profile', 'viewed_user': viewed_user })
