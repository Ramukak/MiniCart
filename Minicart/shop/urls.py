from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',indexView,name="index"),
    path('items',searchProduct,name="item-view"),

]