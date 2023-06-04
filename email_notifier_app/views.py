from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.
def send_notification(request,email):
    message = request.GET["msg"]
    send_mail(
    "Email notification from travel management app",
    message,
    "msmasud578@gmail.com",
    [email],
    fail_silently=False,
    )
    return HttpResponseRedirect("/")