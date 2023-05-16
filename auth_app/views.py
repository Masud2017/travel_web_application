from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def greeting(request):
    return render(request,"homepage.html")

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")