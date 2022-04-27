from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User
from django.db import models


class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class Login(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())