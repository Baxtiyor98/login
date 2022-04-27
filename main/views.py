from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

def register(request):
    return render(request,'index.html')


