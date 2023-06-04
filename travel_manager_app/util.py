from auth_app.models import UserModelExtended,HistoriesOrder,HistoriesCustomOrder,OrderCustomPackages,OrderPackages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import os
import datetime
from pathlib import Path
from django.db.models.functions import TruncMonth,TruncDay

def add_history_order_for_user(user_object,agent_object,order,status):
    history = HistoriesOrder()
    history.user_model_extended = user_object
    history.order = order
    history.status = status
    history.other_user = agent_object

    history.save()

def add_history_order_for_agent(agent_object,user_object,order,status):
    # at fist register user history
    user_model = UserModelExtended.objects.get(user = user_object)
    agent_user = agent_object.user
    add_history_order_for_user(user_object=user_model,agent_object=agent_user,order = order,status = status)
    # second register agent history
    history = HistoriesOrder()
    history.user_model_extended = agent_object
    history.order = order
    history.status = status
    history.other_user = user_object

    history.save()

def add_history_custom_order_for_user(user_object,agent_object,order,status):
    history = HistoriesCustomOrder()
    history.user_model_extended = user_object
    history.custom_order = order
    history.status = status
    history.other_user = agent_object

    history.save()

def add_history_custom_order_for_agent(agent_object,user_object,order,status):
    # at fist register user history
    user_model = UserModelExtended.objects.get(user = user_object)
    agent_user = agent_object.user
    add_history_custom_order_for_user(user_object = user_model,agent_object=agent_user,order = order, status = status)
    # second register agent history

    history = HistoriesCustomOrder()
    history.user_model_extended = agent_object
    history.custom_order = order
    history.status = status
    history.other_user = user_object

    history.save()

def get_revenue_per_month():
    pre_made = OrderPackages.objects.all()
    custom = OrderCustomPackages.objects.all()

    pre_made_month = 0
    custom_month = 0
    current_time = datetime.datetime.now()

    for item in pre_made:
        if item.created_at.month == current_time.month:
            pre_made_month = pre_made_month + item.packages.price

    for item in custom:
        if item.created_at.month == current_time.month:
            custom_month = custom_month + item.custom_packages.price
                

    json = {"pre_made_month":pre_made_month,"custom_month":custom_month}
    return json
    

def get_revenue_daily():
    pre_made = OrderPackages.objects.all()
    custom = OrderCustomPackages.objects.all()

    pre_made_daily = 0
    custom_daily = 0
    current_time = datetime.datetime.now()
    print(current_time.day)
    for item in pre_made:
        print(item.created_at.day)
        if item.created_at.day == current_time.day:
            pre_made_daily = pre_made_daily + item.packages.price

    for item in custom:
        print(item.created_at.day)
        if item.created_at.day == current_time.day:

            custom_daily = custom_daily + item.custom_packages.price
                

    json = {"pre_made_daily":pre_made_daily,"custom_daily":custom_daily}
    return json