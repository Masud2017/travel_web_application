from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import permission_required,login_required
from auth_app.models import Hotels,Flights,Activities,Packages

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
def add_flights(request):
    return render(request,"add_flights.html")

@login_required(login_url="/login")
@permission_required([
    "auth_app.add_flights",
])
def add_new_flight(request):
    name = request.GET["name"]
    flight_from = request.GET["from"]
    flight_to = request.GET["to"]
    travel_date = request.GET["travel_date"]
    title = request.GET["title"]
    flight_image = request.GET["image"]
    price = request.GET["price"]
    stock = request.GET["stock"]
    description = request.GET["description"]

    current_user = request.user.usermodelextended
    
    Flights.objects.create(user_model_exnteded= current_user,name = name,from_dst = flight_from,
                           to_dst = flight_to,travel_date = travel_date,title = title,
                           product_image_url = flight_image,price = price,stock = stock,
                           description = description)
    
    return HttpResponseRedirect("/flights")

    
@login_required(login_url="/login")
def flight_details(request,flight_id):
    flight = Flights.objects.get(id = flight_id)
    return render(request,"flight_details.html",{"flight":flight})

@login_required(login_url="/login")
def activities(request):
    activities = Activities.objects.all()
    return render(request,"activities.html",{"activities":activities})
@login_required(login_url="/login")
def add_activities(request):
    return render(request, "add_activities.html")

@login_required(login_url="/login")
def add_new_activity(request):
    name = request.GET["name"]

    Activities.objects.create()
    return HttpResponseRedirect("/activities")

@login_required(login_url= "/login")
def activity_details(request,activity_id):
    activity = Activities.objects.get(id= activity_id)
    return render(request,"activity_details.html",{"activity":activity})

@login_required(login_url="/login")
def packages(request):
    packages = Packages.objects.all()
    return render(request,"packages.html",{"packages":packages})

@login_required(login_url= "/login")
def package_details(request,package_id):
    package = Packages.objects.get(id = package_id)
    return render(request, "package_details.html",{"package":package})