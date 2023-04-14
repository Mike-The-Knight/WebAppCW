from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def account(request):
    return render(request, 'members/index.html', {'title': 'Account'})

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

def profile(request):
    return render(request, 'members/profile.html', {'title': 'Profile'})