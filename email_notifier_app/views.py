from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.
@login_required(login_url = "/login")
def send_notification(request,email):
    send_mail(
    "Subject here",
    "Here is the message.",
    "msmasud578@gmail.com",
    ["to@yopmail.com"],
    fail_silently=False,
    )
    return HttpResponse("Mail sended to the mail : "+email + "successfuly")