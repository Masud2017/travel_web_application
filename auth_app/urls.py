from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = "index"),
    path('login',views.login_view,name = 'login'),
    path('signup',views.signup,name = 'signup'),
    path('register',views.register,name = 'register'),
    path('do_authenticate',views.authentication,name = 'do_authenticate'),
    path('logout',views.perform_logout,name = 'logout'),
    path('forget_password',views.forget_password,name = 'forget_password'),
    path('change_password',views.change_password,name = 'change_password'),
]
