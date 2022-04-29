from django.urls import path
from .views import *

urlpatterns = [
    #auth
    path('register/',register,name='register'),
    path('log_in/',log_in,name='log_in'),
]