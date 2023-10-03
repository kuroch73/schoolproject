from django.urls import path
# from . import views
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', index),
    path('about', about),
    path('Studentlist', Studentlist, name='Studentlist'),
    path('hello/', hello_world),
    path('login/', LoginView, name='login'),
]
