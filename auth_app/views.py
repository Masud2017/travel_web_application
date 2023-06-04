from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import util
from .models import UserModelExtended,Roles

from django.contrib.auth.models import Group
from .models import Hotels

# Create your views here.

def index(request):
    hotels = Hotels.objects.all()
    if request.user.is_authenticated:
        return render(request,"homepage.html",{"hotels":hotels})
    return render(request,"homepage.html",{"hotels":[]})

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
    retype_password = request.POST["re_pass"]
    name = request.POST["name"]
    profile_image = request.FILES["image"]
    user_type = request.POST["user_type"]

    if password != retype_password:
        messages.add_message(request,messages.INFO, "Password is not matched !!")
        return HttpResponseRedirect("/signup")
    
    
    
    # with open("temp_image","w") as f:
    #     f.write(image_file)

    try:
        user = User.objects.get(email = username)
        # messages.add_message(request, messages.INFO, "Hello world.")
    except Exception:
        new_user = User.objects.create(username = username, email = username, first_name = name)
        new_user.set_password(password)
        new_user.save()

        

        # assign user to a group
        if user_type == "agent":
            # adding user_profile image url into the extended user model
            user_model_extended = UserModelExtended.objects.create(user = new_user,image_url = util.save_image_to_disk(profile_image),role = util.get_role_by_role_string("agent"))
            user_model_extended.save()

            agent_group, created = Group.objects.get_or_create(name='agent')
            new_user.groups.add(agent_group)
        elif user_type == "user":
            # adding user_profile image url into the extended user model
            user_model_extended = UserModelExtended.objects.create(user = new_user,image_url = util.save_image_to_disk(profile_image),role = util.get_role_by_role_string("user"))
            user_model_extended.save()

            user_group, created = Group.objects.get_or_create(name='user')
            new_user.groups.add(user_group)

        
        print("User not found")

    return HttpResponseRedirect("/signup")
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


def forget_password(request):
    email = request.GET["email"]

    import datetime
    print(datetime.datetime.now().microsecond) 

@login_required(login_url= "/login")
def change_password(request):
    password = request.POST["password"]
    email = request.user.email

    user =User.objects.get(email = email)
    user.set_password(password)
    user.save()

    return HttpResponseRedirect("/")