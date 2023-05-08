from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='http://127.0.0.1:8000/members/account/signin')
def chat_room(request):
    return render(request, 'chat/chat_room.html')

