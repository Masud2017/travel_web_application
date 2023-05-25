from .models import UserModelExtended,Roles
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import os

def save_image_to_disk(file_obj):
    path = "C:/travel_management_webapp_image_storage/"
    if os.path.exists(path + file_obj.name): 
        with open(path + file_obj.name,"wb+") as f:
            for chunk_item in file_obj.chunks():
                f.write(chunk_item)
    else:
        os.makedirs(path)
        with open(path + file_obj.name,"wb+") as f:
            for chunk_item in file_obj.chunks():
                f.write(chunk_item)
    

    return path+file_obj.name

def get_saved_image_from_disk(current_user):
    try:
        user_model_extended_obj = current_user.user_model_extended
    except ObjectDoesNotExist:
        print("UserModelExtended object not available for the given user object")