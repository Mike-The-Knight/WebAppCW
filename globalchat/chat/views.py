from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

def index(request):
    return render(request, "chat/index.html")