from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('home/', views.index)
]
