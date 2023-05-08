from django.urls import path, include
from chat import views as chat_views
 
 
urlpatterns = [
    path('room/', chat_views.chat_room, name='chat_room'),
]