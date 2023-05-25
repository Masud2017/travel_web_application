from django.contrib import admin
from .models import Roles,UserModelExtended,Flights,Activities,Hotels,Packages,CustomPackages,Orders,Cancellations

# Register your models here.
admin.site.register(Roles)
admin.site.register(UserModelExtended)

admin.site.register(Flights)
admin.site.register(Activities)
admin.site.register(Hotels)
admin.site.register(Packages)
admin.site.register(CustomPackages)
admin.site.register(Orders)
admin.site.register(Cancellations)