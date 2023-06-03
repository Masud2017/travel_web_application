from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("auth_app.urls")),
    path('',include("travel_manager_app.urls")),
    path('',include("payment_app.urls")),
    path('',include("email_notifier_app.urls"))

]
