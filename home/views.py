from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("This is Home page")


def aboutus(request):
    return HttpResponse("This is About Us page")


def contactus(request):
    return HttpResponse("This is Contact Us page")
