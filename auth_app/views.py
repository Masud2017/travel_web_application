from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import util
from .models import UserModelExtended,Roles

# Create your views here.

def index(request):
    return render(request,"homepage.html")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    return render(request,"login.html")

def signup(request):
    if request.user.is_authenticated:
        return redirect("/")
        
    return render(request,"signup.html")

def register(request):
    username = request.POST["username"]
    password = request.POST["password"]
    name = request.POST["name"]
    profile_image = request.FILES["image"]

    
    
    # with open("temp_image","w") as f:
    #     f.write(image_file)

    try:
        user = User.objects.get(email = username)
        # messages.add_message(request, messages.INFO, "Hello world.")
    except Exception:
        new_user = User.objects.create(username = username, email = username, first_name = name)
        new_user.set_password(password)
        new_user.save()

        # adding user_profile image url into the extended user model
        user_model_extended = UserModelExtended(user = new_user,image_url = util.save_image_to_disk(profile_image))
        user_model_extended.save()
        
        print("User not found")
    # if user != None:
    #     print("User is not null")


    return HttpResponse("hello world")
def authentication(request):
    username = request.POST["username"]
    password = request.POST["password"]

    print("password checked")
    user_auth = authenticate(username = username,password = password)
    if user_auth is not None:
        print("loggingin")
        login(request,user_auth)
    else:
        messages.add_message(request, messages.INFO, "This credential does not exist please recheck your username or password!!")

    
    return redirect("/login")

def perform_logout(request):
    logout(request)
    return redirect("/login")