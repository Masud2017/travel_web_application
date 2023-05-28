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

    current_user = request.user
    handler = ProductHandler(current_user)
    handler.add_flight(flight_from,flight_to,price,flight_image)

    return HttpResponseRedirect("/")