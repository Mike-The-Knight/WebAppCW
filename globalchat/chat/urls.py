from django.urls import path, include
from chat import views as chat_views
 
 
urlpatterns = [
    path("", chat_views.index, name="index"),
    path("chat/<str:room_name>/", chat_views.room, name="room"),
]