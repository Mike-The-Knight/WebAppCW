#Create the full user sign up form
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':"e.g. bobsmith123"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':"e.g. bobsmith123@gmail.com", 'type':'email'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':"*******", 'type':'password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':"*******", 'type':'password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


#Create the full user update form
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']