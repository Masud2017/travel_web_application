from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.models import Group

# creation of role groups
user_group, created = Group.objects.get_or_create(name='user')
agent_group, created = Group.objects.get_or_create(name='agent')
superuser_group, created = Group.objects.get_or_create(name='superuser')



class Roles(models.Model):
    role_type = models.CharField(max_length=100,default = "")
    role = models.IntegerField()

    class Meta:
        verbose_name_plural = "Roles"

class UserModelExtended(models.Model):
    # USER = 1
    # AGENT = 2
    # SUPERUSER =3
      
    # ROLE_CHOICES = (
    #     (USER, 'User'),
    #     (AGENT, 'Agent'),
    #     (SUPERUSER, 'Superuser'))

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.ForeignKey(Roles,on_delete= models.CASCADE,blank=True,null = True) # Many to one relationship with the Roles model
    # role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

    image_url = models.CharField(max_length=100,default = "https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png")

    class Meta:
        verbose_name_plural = "UserModelExtended"
        permissions = (
            ("can_create_hotels","User that has this permission enable can create hotel as individual product"),
            ("can_create_flights","User that has this permission enable can create flight as individual product"),
            ("can_create_activities","User that has this permission enable can create activities as individual product"),
            ("can_create_packages","User that has this permission enable can create package as individual product"),
            ("can_create_custom_packages","User that has this permission enable can create custom package as individual product"),
            
            ("can_edit_hotels","User that has this permission enable can edit hotel as individual product"),
            ("can_edit_flights","User that has this permission enable can edit flight as individual product"),
            ("can_edit_activities","User that has this permission enable can edit activity as individual product"),
            ("can_edit_packages","User that has this permission enable can edit package as individual product"),
            ("can_edit_custom_packages","User that has this permission enable can edit custom package as individual product"),
            
            ("can_delete_hotels","User that has this permission enable can delete hotel as individual product"),
            ("can_delete_flights","User that has this permission enable can delete flight as individual product"),
            ("can_delete_activities","User that has this permission enable can delete activity as individual product"),
            ("can_delete_packages","User that has this permission enable can delete package as individual product"),
            ("can_delete_custom_packages","User that has this permission enable can delete custom package as individual product"),

            ("can_remove_user","User that has this permission enable can remove any user except superuser"),
            ("can_create_user","User that has this permission enable can create new account an user (both agent and user)"),
            ("can_cancel_order","User that has this permission enable can cancel order based on user request"),
            ("can_place_order","User that has this permission enable can place new order"),
            ("can_create_new_permission", "User that has this permission enabled can create new permissions for a specific role type"),
            ("can_create_new_role", "User that has this permission enabled can create new role with permissions"),
            ("can_use_account", "User need this permission enabled to be able to use his/her account"),
        )

class Flights(models.Model):
    from_dst = models.CharField(max_length=200)
    to_dst = models.CharField(max_length=200)
    travel_date = models.DateField()
    product_image_url = models.CharField(max_length = 200,default = "https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png")

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


class Cancellations(models.Model):
    user_model_extended = models.OneToOneField(UserModelExtended,on_delete=models.CASCADE,default = None)

    flight = models.ForeignKey(Flights,on_delete=models.CASCADE)
    activity = models.ForeignKey(Activities,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name_plural = "Cancellations"
        


