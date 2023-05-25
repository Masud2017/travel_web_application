from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Roles(models.Model):
    role = models.IntegerField()

    class Meta:
        verbose_name_plural = "Roles"

class UserModelExtended(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.ForeignKey(Roles,on_delete= models.CASCADE,blank=True,null = True) # Many to one relationship with the Roles model
    image_url = models.CharField(max_length=100,default = "no_image_url_available")


class Flights(models.Model):
    from_dst = models.CharField(max_length=200)
    to_dst = models.CharField(max_length=200)
    travel_date = models.DateField()

    class Meta:
        verbose_name_plural = "Flights"

class Activities(models.Model):
    activity_type = models.IntegerField()

    class Meta:
        verbose_name_plural = "Activities"

class Hotels(models.Model):
    room_count = models.IntegerField()
    price = models.IntegerField()
    room_size = models.IntegerField()

    class Meta:
        verbose_name_plural = "Hotels"

class Packages(models.Model):
    flight = models.ForeignKey(Flights,on_delete=models.CASCADE)
    activity = models.ForeignKey(Activities,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Packages"

class CustomPackages(models.Model):
    user = models.ForeignKey(UserModelExtended,on_delete=models.CASCADE,default = None)

    flight = models.ForeignKey(Flights,on_delete=models.CASCADE)
    activity = models.ForeignKey(Activities,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "CustomPackages"


class Orders(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    is_package = models.BooleanField(default = False)
    packages = models.ManyToManyField(Packages)
    custom_packages = models.ManyToManyField(CustomPackages)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name_plural = "Orders"


class Cancellations(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    flight = models.ForeignKey(Flights,on_delete=models.CASCADE)
    activity = models.ForeignKey(Activities,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name_plural = "Cancellations"
        


