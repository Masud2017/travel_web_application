from django.contrib import admin
from .models import Roles,UserModelExtended

# Register your models here.
admin.site.register(Roles)
admin.site.register(UserModelExtended)