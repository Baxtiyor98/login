from django.urls import path
from .views import *

urlpatterns = [
    #auth
    path('',register,name='register'),
]