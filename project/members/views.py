from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def account(request):
    return render(request, 'members/index.html', {'title': 'Account'})

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        firstname = request.POST['firstname']
        surname = request.POST['surname']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        newuser = User.objects.create_user(username, email, password)
        newuser.first_name = firstname
        newuser.last_name = surname

        newuser.save()

        messages.success(request, "Your account has been successfully created")

        return redirect('signin')
    else:
        return render(request, 'members/signup.html', {'title': 'Sign up'})

    

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return render(request, "members/index.html", {'fname': user.first_name})
        else:
            messages.error(request, "Incorrect username or password")
            return redirect("account")

    else:
        return render(request, 'members/signin.html', {'title': 'Sign in'})

def signout(request):
    logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect("index")