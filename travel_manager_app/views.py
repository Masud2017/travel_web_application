from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import permission_required,login_required
from auth_app.models import Hotels,Flights

from .services.ProductHandler import ProductHandler

# Create your views here.
@login_required
def product_details(request,hotel_id):
    hotel = Hotels.objects.get(id = hotel_id)

    return render(request,"product_details.html",{"hotel":hotel})

def add_hotel_page(request):
    return render(request,"add_hotels.html")


@login_required(login_url="/login")
@permission_required([
    "auth_app.add_hotels",
],login_url="/login")
def add_new_hotel(requeset):
    hotel_name = requeset.GET["name"]
    room_size = requeset.GET["size"]
    room_count = requeset.GET["count"]
    product_image = requeset.GET["image"]
    description = requeset.GET["description"]
    title = requeset.GET["title"]
    price = requeset.GET["price"]
    stock = requeset.GET["stock"]
    address = requeset.GET["address"]

    current_user = requeset.user.usermodelextended

    Hotels.objects.create(
        user_model_exnteded = current_user,
        name = hotel_name,
        room_count = room_count,
        room_size = room_size,
        product_image_url = product_image,
        description = description,
        title = title,
        price = price,
        stock = stock,
        address = address
    )

    return HttpResponseRedirect("/")


def edit_hotel(request,hotel_id):

    hotel = Hotels.objects.get(id = hotel_id)
    pass

@login_required(login_url="/login")
@permission_required([
    "auth_app.delete_hotels",
    ],login_url="/login")
def delete_hotel(request,hotel_id):
    print("printing the value of hotel id : ",hotel_id)
    hotel = Hotels.objects.get(id = hotel_id)
    hotel.delete()

    return HttpResponseRedirect("/")

@login_required(login_url="/login")
def flights(request):
    flights = Flights.objects.all()
    return render(request,"flights.html",{"flights":flights})


@login_required(login_url="/login")
@permission_required([
    "add_flights",
])
def add_new_flight(request):
    flight_from = request.GET["from"]
    flight_to = request.GET["to"]
    flight_image = request.GET["image"]
    price = request.GET["price"]
    stock = request.GET["stock"]
    description = request.GET["description"]

    current_user = request.user
    handler = ProductHandler(current_user)
    flight_handler = handler.FlightHandler(current_user = current_user)
    
    is_done = flight_handler.add_flight(flight_from= flight_from, flight_to = flight_to, price = price
                              ,flight_image = flight_image,stock = stock,description = description)
    
    if is_done:
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/error")
        