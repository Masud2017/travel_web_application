from .models import UserModelExtended,Roles
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import os
import datetime
from pathlib import Path

def change_name_and_return_image_obj(image_obj):
    date = str(datetime.datetime.now())
    date = date.replace("-","_")
    date = date.replace(" ","_")
    date = date.replace(":","_")
    date = date.replace(".","_")
    extension = image_obj.name.split(".")[1]
    image_obj.name = date + "." +extension

    return image_obj

def save_image_to_disk(file_obj):
    # path = "C:/travel_management_webapp_image_storage/"
    BASE_DIR = Path(__file__).resolve().parent.parent
    path = os.path.join(BASE_DIR,"static/storage/")
    file_obj = change_name_and_return_image_obj(file_obj)
    if os.path.exists(path): 
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


def get_role_by_role_string(user_role_string):
    role = Roles.objects.get(role_type = user_role_string)

    return role