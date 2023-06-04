from django.urls import path
from . import views

urlpatterns = [
    path('send_notification/<str:email>',views.send_notification,name = "send_notification"),
    
]
