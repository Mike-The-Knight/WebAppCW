"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from .views import Follow, SetPicture

urlpatterns = [
    path('account', views.account, name='account'),
    path('account/update', views.update_account, name='update_account'),
    path('account/signup', views.signup, name="signup"),
    path('account/signin', views.signin, name="signin"),
    path('account/signout', views.signout, name="signout"),

    # view a users profile page
    path('<int:pk>/', views.view_user, name="view_user"),

    # add/remove friends
    path('<int:pk>/follow', Follow.as_view(), name='follow'),

    # add/remove friends
    path('setpicture/<int:pk>', SetPicture.as_view(), name='setpicture')
]


