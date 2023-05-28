from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import permission_required,login_required

from .services.ProductHandler import ProductHandler

# Create your views here.
@login_required(login_url="/login")
@permission_required([
    "add_flights",
    "add_flights_for_user"
])
def add_new_flight(request):
    flight_from = request.GET["from"]
    flight_to = request.GET["to"]
    flight_image = request.GET["image"]
    price = request.GET["price"]
    stock = request.GET["stock"]

    current_user = request.user
    handler = ProductHandler(current_user)
    handler.add_flight(flight_form = flight_from
                       ,flight_to = flight_to,price = price
                       ,flight_image = flight_image
                       ,stock = stock)

    return HttpResponseRedirect("/")