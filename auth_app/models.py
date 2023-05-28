from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.models import Group,Permission

# creation of role groups
# user group
user_group, created = Group.objects.get_or_create(name='user')
user_group.permissions.add(Permission.objects.get(codename = "add_orders"))
user_group.permissions.add(Permission.objects.get(codename = "change_orders"))
user_group.permissions.add(Permission.objects.get(codename = "delete_orders"))
user_group.permissions.add(Permission.objects.get(codename = "view_orders"))
user_group.permissions.add(Permission.objects.get(codename = "add_cancellations"))
user_group.permissions.add(Permission.objects.get(codename = "change_cancellations"))
user_group.permissions.add(Permission.objects.get(codename = "delete_cancellations"))
user_group.permissions.add(Permission.objects.get(codename = "view_cancellations"))
user_group.permissions.add(Permission.objects.get(codename = "view_flights"))
user_group.permissions.add(Permission.objects.get(codename = "view_hotels"))
user_group.permissions.add(Permission.objects.get(codename = "view_activities"))
user_group.permissions.add(Permission.objects.get(codename = "view_packages"))
user_group.permissions.add(Permission.objects.get(codename = "add_custompackages"))
user_group.permissions.add(Permission.objects.get(codename = "change_custompackages"))
user_group.permissions.add(Permission.objects.get(codename = "delete_custompackages"))
user_group.permissions.add(Permission.objects.get(codename = "view_custompackages"))
user_group.permissions.add(Permission.objects.get(codename = "add_histories"))
user_group.permissions.add(Permission.objects.get(codename = "delete_histories"))
user_group.permissions.add(Permission.objects.get(codename = "view_histories"))

# user_group.permissions.add(Permission.objects.get(codename = "can_create_flights"))

# agent group
agent_group, created = Group.objects.get_or_create(name='agent')
agent_group.permissions.add(Permission.objects.get(codename = "add_flights"))
agent_group.permissions.add(Permission.objects.get(codename = "view_flights"))
agent_group.permissions.add(Permission.objects.get(codename = "change_flights"))
agent_group.permissions.add(Permission.objects.get(codename = "delete_flights"))
agent_group.permissions.add(Permission.objects.get(codename = "add_orders_for_user"))
agent_group.permissions.add(Permission.objects.get(codename = "change_orders_for_user"))
agent_group.permissions.add(Permission.objects.get(codename = "delete_orders_for_user"))
agent_group.permissions.add(Permission.objects.get(codename = "view_orders_for_user"))
agent_group.permissions.add(Permission.objects.get(codename = "add_cancellations_for_user"))
agent_group.permissions.add(Permission.objects.get(codename = "view_cancellations_for_user"))
agent_group.permissions.add(Permission.objects.get(codename = "change_cancellations_for_user"))
agent_group.permissions.add(Permission.objects.get(codename = "delete_cancellations_for_user"))

# super user group
superuser_group, created = Group.objects.get_or_create(name='superuser')
# we need this permission thing while we are going to work with agent handling and security stuff

# Assiging database models for django orm
class Roles(models.Model):
    role_type = models.CharField(max_length=100,default = "")
    role = models.IntegerField()

    class Meta:
        verbose_name_plural = "Roles"

class UserModelExtended(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.ForeignKey(Roles,on_delete= models.CASCADE,blank=True,null = True) # Many to one relationship with the Roles model

    image_url = models.CharField(max_length=100,default = "https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png")

    class Meta:
        verbose_name_plural = "UserModelExtended"
        permissions = (
            ("can_use_account", "User need this permission enabled to be able to use his/her account"),
        )

class Flights(models.Model):
    user_model_exnteded = models.ForeignKey(UserModelExtended,on_delete=models.CASCADE,default = None, null = True, blank = True)

    from_dst = models.CharField(max_length=200)
    to_dst = models.CharField(max_length=200)
    travel_date = models.DateTimeField(default = None,null = True, blank = True)
    product_image_url = models.CharField(max_length = 200,default = "https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png")
    created_at = models.DateTimeField(auto_now_add = True,null = True, blank = True)
    updated_at = models.DateTimeField(auto_now = True,null = True, blank = True)
    price = models.IntegerField(default = 0)
    stock = models.IntegerField(default = 0)

    class Meta:
        verbose_name_plural = "Flights"

class Activities(models.Model):
    activity_type = models.IntegerField()
    product_image_url = models.CharField(max_length = 200,default = "https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png")

    class Meta:
        verbose_name_plural = "Activities"

class Hotels(models.Model):
    room_count = models.IntegerField()
    price = models.IntegerField()
    room_size = models.IntegerField()
    product_image_url = models.CharField(max_length = 200,default = "https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png")

    class Meta:
        verbose_name_plural = "Hotels"

class Packages(models.Model):
    user_model_extended = models.ForeignKey(UserModelExtended,on_delete=models.CASCADE,default = None)
    
    flight = models.ForeignKey(Flights,on_delete=models.CASCADE)
    activity = models.ForeignKey(Activities,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Packages"

class CustomPackages(models.Model):
    user_model_extended = models.ForeignKey(UserModelExtended,on_delete=models.CASCADE,default = None, null = True)

    flight = models.ForeignKey(Flights,on_delete=models.CASCADE)
    activity = models.ForeignKey(Activities,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "CustomPackages"


class Orders(models.Model):
    user_model_extended = models.OneToOneField(UserModelExtended,on_delete=models.CASCADE,default = None)

    is_package = models.BooleanField(default = False)
    packages = models.ManyToManyField(Packages)
    custom_packages = models.ManyToManyField(CustomPackages)
    is_paid =  models.BooleanField(default = False)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name_plural = "Orders"
        permissions = (
            ("add_orders_for_user", "add orders for user"),
            ("change_orders_for_user","change orders for user"),
            ("delete_orders_for_user","delete orders for user"),
            ("view_orders_for_user", "view orders for user")
        )


class Cancellations(models.Model):
    user_model_extended = models.OneToOneField(UserModelExtended,on_delete=models.CASCADE,default = None)

    flight = models.ForeignKey(Flights,on_delete=models.CASCADE)
    activity = models.ForeignKey(Activities,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name_plural = "Cancellations"
        permissions = (
            ("add_cancellations_for_user","cancel for user"),
            ("view_cancellations_for_user","view cancellations for user"),
            ("delete_cancellations_for_user","delete cancellations for user"),
            ("change_cancellations_for_user","change cancellations for user"),
        )
        

class Histories(models.Model):
    user_model_extended = models.ForeignKey(UserModelExtended,on_delete=models.CASCADE)
    product_id = models.IntegerField(default = None,null = True, blank = True) # product can be anything (hotels, activities,flights,packages,custom packages)
    description = models.CharField(max_length = 255,default = "No description available",null = True, blank = True)

    class Meta:
        verbose_name_plural = "Histories"