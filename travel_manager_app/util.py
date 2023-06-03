from auth_app.models import UserModelExtended,HistoriesOrder,HistoriesCustomOrder
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import os
import datetime
from pathlib import Path

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