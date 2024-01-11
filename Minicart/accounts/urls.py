from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('login',loginUser,name='login'),
    path('register',registerUser,name='register'),
    path('otp',otpView,name='otp'),
    
    
]