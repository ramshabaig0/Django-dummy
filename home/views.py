from django.shortcuts import render, HttpResponse

# Create your views here.


def index():
    return HttpResponse("This is Home page")
