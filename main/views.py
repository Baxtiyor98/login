from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

def register(request):
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password2==password1:
                user = authenticate(request,username=username, password=password1)
                if user is not None:
                    login(request,user)
                    return redirect('log_in')
    return render(request, 'register.html')

def log_in(request):
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password1 = request.POST.get('password')
            user = authenticate(request,username=username, password=password1)
            if user is not None:
                login(request,user)
                return redirect('register')
    return render(request, 'login.html')


