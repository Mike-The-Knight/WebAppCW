from django.shortcuts import render, redirect

# Create your views here.
def chat(request, *args, **kwargs):
  if not request.user.is_authenticated:
    return redirect("signin")
  context = {}
  return render(request, "chat/chat_page.html", context)

def room(request, room_name):
  return render(request, "chat/room.html", {"room_name": room_name})
