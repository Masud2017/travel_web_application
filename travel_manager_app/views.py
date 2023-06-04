from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import permission_required,login_required
from auth_app.models import Hotels,Flights,Activities,Packages,CustomPackages,OrderCustomPackages,OrderPackages,HistoriesOrder,HistoriesCustomOrder,Roles
from django.contrib.auth.models import User
from .services.ProductHandler import ProductHandler
from . import util

# Create your views here.
@login_required
def product_details(request,hotel_id):
    hotel = Hotels.objects.get(id = hotel_id)
    package= None
    package = CustomPackages.objects.filter(is_done = False,user_model_extended = request.user.usermodelextended).first()
    if package == None:
        package = CustomPackages.objects.create(user_model_extended = request.user.usermodelextended)


    return render(request,"product_details.html",{"hotel":hotel,"package":package})

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
@permission_required([
    "auth_app.delete_flights",
    ],login_url="/login")
def delete_hotel(request,flight_id):
    flight = Flights.objects.get(id = flight_id)
    flight.delete()

    return HttpResponseRedirect("/flights")

def delete_package(request,package_id):
    package = Packages.objects.get(id = package_id)
    package.is_done = False
    package.save()

    return HttpResponseRedirect("/packages")

def delete_custom_package(request,package_id):
    package = CustomPackages.objects.get(id = package_id)
    # package.delete()
    package.is_done = False
    package.save()

    return HttpResponseRedirect("/custom_packages")

def delete_activity(request,activity_id):
    activity = Activities.objects.get(id = activity_id)
    activity.delete()

    return HttpResponseRedirect("/activities")

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
    package=  CustomPackages.objects.filter(is_done = False,user_model_extended = request.user.usermodelextended).first()

    if package == None:
        package = CustomPackages.objects.create(user_model_extended = request.user.usermodelextended)

    return render(request,"flight_details.html",{"flight":flight,"package":package})

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
    custom_package = CustomPackages.objects.filter(is_done = False,user_model_extended = request.user.usermodelextended).first()
    if custom_package == None:
        custom_package = CustomPackages.objects.create(user_model_extended = request.user.usermodelextended)
    return render(request,"activity_details.html",{"activity":activity,"package":custom_package})

@login_required(login_url="/login")
def packages(request):
    packages = Packages.objects.all()
    return render(request,"packages.html",{"packages":packages})

@login_required(login_url= "/login")
def package_details(request,package_id):
    package = Packages.objects.get(id = package_id)
    return render(request, "package_details.html",{"package":package})

@login_required(login_url="/login")
# @permission_required(["auth_app.add_packages"],login_url= "/login")
def select_hotel_for_package(request,package_id,hotel_id):
    hotel_qty = request.GET["hotel_qty"]
    hotel = Hotels.objects.get(id = hotel_id)
    Packages.objects.filter(id = package_id).update(hotel = hotel,hotel_qty = hotel_qty)

    return HttpResponseRedirect("/add_packages/"+str(package_id))

@login_required(login_url="/login")
# @permission_required(["auth_app.add_packages"],login_url="/login")
def add_packages(request,package_id = None):
    if (package_id != None):
        package = Packages.objects.get(id = package_id)
        hotels = Hotels.objects.all()
        flights = Flights.objects.all()

        activity_list = package.activities.all()
        activity_id_list = []

        for x in activity_list:
            activity_id_list.append(x.id)

        activities = Activities.objects.exclude(id__in = activity_id_list)

        
        return render(request, "add_packages.html", {"hotels":hotels,"flights":flights,"activities":activities,"package":package})
    else:
        package = None
        if Packages.objects.filter(is_done = False).count() == 0:
            Packages.objects.create(user_model_extended = request.user.usermodelextended)
        else:
            package = Packages.objects.filter(is_done = False).first()
            hotels = Hotels.objects.all()
            flights = Flights.objects.all()
            activities = Activities.objects.all()
            return render(request, "add_packages.html", {"hotels":hotels,"flights":flights,"activities":activities,"package":package})
        


@login_required(login_url="/login")
# @permission_required(["add_packages"],login_url= "/login")
def select_flight_for_package(request,package_id,flight_id):
    flight_qty = request.GET["flight_qty"]
    flight = Flights.objects.get(id = flight_id)
    Packages.objects.filter(id = package_id).update(flight = flight,flight_qty = flight_qty)

    return HttpResponseRedirect("/add_packages/"+str(package_id))



@login_required(login_url="/login")
# @permission_required(["add_packages"],login_url= "/login")
def select_activity_for_package(request,package_id,activity_id):
    # flight_qty = request.GET["_qty"]
    activity = Activities.objects.get(id = activity_id)
    # Packages.objects.filter(id = package_id).update(activities = activity)
    package = Packages.objects.get(id = package_id)
    package.activities.add(activity)

    return HttpResponseRedirect("/add_packages/"+str(package_id))

@login_required(login_url="/login")
# @permission_required(["add_packages"],login_url= "/login")
def deselect_activity_for_package(request,package_id,activity_id):
    # flight_qty = request.GET["_qty"]
    activity = Activities.objects.get(id = activity_id)
    # Packages.objects.filter(id = package_id).update(activities = activity)
    package = Packages.objects.get(id = package_id)
    package.activities.remove(activity)

    return HttpResponseRedirect("/add_packages/"+str(package_id))

@login_required(login_url="/login")
def save_package(request,package_id):
    name = request.GET["name"]
    title = request.GET["title"]
    description = request.GET["desc"]

    package = Packages.objects.get(id = package_id)
    package.is_done = True

    package.name = name

    activity_price = 0
    for item in package.activities.all():
        activity_price = activity_price + item.price

    package.price = (package.hotel_qty * package.hotel.price) + (package.flight.price * package.flight_qty) + activity_price
    package.title = title

    package.description = description

    package.save()

    return HttpResponseRedirect("/packages")

# custom package section started

@login_required(login_url="/login")
@permission_required(["auth_app.add_custompackages"],login_url= "/login")
def custom_packages(request):
    packages = CustomPackages.objects.all()

    return render(request,"custom_packages.html", {"packages":packages})

@login_required(login_url='/login')
@permission_required(["auth_app.add_custompackages"],login_url="/login")
def add_custom_packages(request,package_id = None):
    if (package_id != None):
        package = CustomPackages.objects.get(id = package_id)
        hotels = Hotels.objects.all()
        flights = Flights.objects.all()

        activity_list = package.activities.all()
        activity_id_list = []

        for x in activity_list:
            activity_id_list.append(x.id)

        activities = Activities.objects.exclude(id__in = activity_id_list)

        
        return render(request, "add_custom_packages.html", {"hotels":hotels,"flights":flights,"activities":activities,"package":package})
    else:
        package = None
        if CustomPackages.objects.filter(is_done = False,user_model_extended = request.user.usermodelextended).count() == 0:
            CustomPackages.objects.create(user_model_extended = request.user.usermodelextended)
        else:
            package = CustomPackages.objects.filter(is_done = False,user_model_extended = request.user.usermodelextended).first()
            hotels = Hotels.objects.all()
            flights = Flights.objects.all()
            activities = Activities.objects.all()
            return render(request, "add_custom_packages.html", {"hotels":hotels,"flights":flights,"activities":activities,"package":package})
        





@login_required(login_url="/login")
def save_custom_package(request,package_id):
    name = request.GET["name"]
    title = request.GET["title"]
    description = request.GET["desc"]

    package = CustomPackages.objects.get(id = package_id)
    package.is_done = True

    package.name = name

    activity_price = 0
    for item in package.activities.all():
        activity_price = activity_price + item.price

    package.price = (package.hotel_qty * package.hotel.price) + (package.flight.price * package.flight_qty) + activity_price
    package.title = title

    package.description = description

    package.save()

    return HttpResponseRedirect("/custom_packages")

@login_required(login_url="/login")
# @permission_required(["add_packages"],login_url= "/login")
def select_hotel_for_custom_package(request,package_id = None,hotel_id = None):
    hotel_qty = request.GET["hotel_qty"]
    hotel = Hotels.objects.get(id = hotel_id)
        
    CustomPackages.objects.filter(id = package_id).update(hotel = hotel,hotel_qty = hotel_qty)

    return HttpResponseRedirect("/add_custom_packages/"+str(package_id))


@login_required(login_url="/login")
# @permission_required(["add_packages"],login_url= "/login")
def select_flight_for_custom_package(request,package_id,flight_id):
    flight_qty = request.GET["flight_qty"]
    flight = Flights.objects.get(id = flight_id)
    CustomPackages.objects.filter(id = package_id).update(flight = flight,flight_qty = flight_qty)

    return HttpResponseRedirect("/add_custom_packages/"+str(package_id))



@login_required(login_url="/login")
# @permission_required(["add_packages"],login_url= "/login")
def select_activity_for_custom_package(request,package_id,activity_id):
    # flight_qty = request.GET["_qty"]
    activity = Activities.objects.get(id = activity_id)
    # Packages.objects.filter(id = package_id).update(activities = activity)
    package = CustomPackages.objects.get(id = package_id)
    package.activities.add(activity)

    return HttpResponseRedirect("/add_custom_packages/"+str(package_id))

@login_required(login_url="/login")
# @permission_required(["add_packages"],login_url= "/login")
def deselect_activity_for_custom_package(request,package_id,activity_id):
    # flight_qty = request.GET["_qty"]
    activity = Activities.objects.get(id = activity_id)
    # Packages.objects.filter(id = package_id).update(activities = activity)
    package = CustomPackages.objects.get(id = package_id)
    package.activities.remove(activity)

    return HttpResponseRedirect("/add_custom_packages/"+str(package_id))

@login_required(login_url="/login")
@permission_required(["auth_app.view_custompackages"],login_url="/login")
def custom_packages_details(request,package_id):
    custom_package = CustomPackages.objects.get(id = package_id)
    return render(request,"custom_package_details.html", {"package":custom_package})



@login_required(login_url="/login")
@permission_required(["auth_app.add_orderpackages"], login_url="/login")
def order_package(request,package_id):
    package = Packages.objects.get(id = package_id)
    
    hotel = package.hotel
    hotel_qty = package.hotel_qty
    flight = package.flight
    flight_qty = package.flight_qty
    activities = package.activities.all()
    
    # first need to check whether any of these products are out of stock
    # second need to deduct qty from subsequent products (hotels,flights)
    if hotel.stock >= hotel_qty:
        # then it is ok
        hotel.stock = hotel.stock - hotel_qty
        hotel.save()
    else:
        # then it is not ok
        
        pass

    if flight.stock >= flight_qty:
        # then it is ok
        flight.stock = flight.stock - flight_qty
        flight.save()
    else:
        # then it is not ok
        pass
    
    return HttpResponseRedirect("/checkout_package/"+str(package_id))


@login_required(login_url="/login")
@permission_required(["auth_app.add_ordercustompackages"], login_url="/login")
def order_custom_package(request,package_id):
    package = CustomPackages.objects.get(id = package_id)
    
    hotel = package.hotel
    hotel_qty = package.hotel_qty
    flight = package.flight
    flight_qty = package.flight_qty
    activities = package.activities.all()
    
    # first need to check whether any of these products are out of stock
    # second need to deduct qty from subsequent products (hotels,flights)
    if hotel.stock >= hotel_qty:
        # then it is ok
        hotel.stock = hotel.stock - hotel_qty
        hotel.save()
    else:
        # then it is not ok
        
        pass

    if flight.stock >= flight_qty:
        # then it is ok
        flight.stock = flight.stock - flight_qty
        flight.save()
    else:
        # then it is not ok
        pass
    
    return HttpResponseRedirect("/checkout_custom_package/"+str(package_id))


@login_required
def myorders(request):
    order_package = OrderPackages.objects.all()
    order_custom_package = OrderCustomPackages.objects.all()

    return render(request, "myorders.html", {"order_packages":order_package, "order_custom_packages":order_custom_package})


@login_required(login_url="/login")
def add_history(request,status,order_id,other_user_id = None):
    if (request.user.usermodelextended.role.role == 1): # agent
        other_user = User.objects.get(id = other_user_id)
        order = OrderPackages.objects.get(id = order_id)
        util.add_history_order_for_agent(request.user.usermodelextended,other_user,order,status)
    else:
        order = OrderPackages.objects.get(id = order_id)
        util.add_history_order_for_user(request.user.usermodelextended,other_user_id,order,status)

    return HttpResponseRedirect("/")

@login_required
def add_custom_history(request,status,order_id,other_user_id = None):
    if (request.user.usermodelextended.role.role == 1): # agent
        other_user = User.objects.get(id = other_user_id)
        order = OrderCustomPackages.objects.get(id = order_id)
        util.add_history_custom_order_for_agent(request.user.usermodelextended,other_user,order,status)
    else:
        order = OrderCustomPackages.objects.get(id = order_id)
        util.add_history_custom_order_for_user(request.user.usermodelextended,other_user_id,order,status)

    return HttpResponseRedirect("/")

@login_required(login_url="/login")
def histories(request):
    histories_order = HistoriesOrder.objects.filter(user_model_extended = request.user.usermodelextended)
    histories_custom_order = HistoriesCustomOrder.objects.filter(user_model_extended = request.user.usermodelextended)
    return render(request, "histories.html", {"histories_order":histories_order, "histories_custom_order":histories_custom_order})


@login_required(login_url="/login")
def user_contacts(request):
    users = User.objects.all()

    return render(request,"user_contacts.html", {"users":users})


@login_required(login_url="/login")
def revenue(request):
    order_pre_made = OrderPackages.objects.all().order_by("-created_at")
    order_custom = OrderCustomPackages.objects.all().order_by("-created_at")
    total_revenue = 0
    for item in order_pre_made:
        total_revenue = total_revenue + item.packages.price
    for item in order_custom:
        total_revenue = total_revenue + item.custom_packages.price

    revenue_month = util.get_revenue_per_month()
    revenue_daily = util.get_revenue_daily()
    return render(request,"revenue.html",{"total_revenue":total_revenue,"order_pre_made":order_pre_made,"order_custom":order_custom,"revenue_month":revenue_month, "revenue_daily":revenue_daily})

@login_required(login_url= "/login")
def search_hotel(request):
    search_query = request.GET["query"]
    hotels = Hotels.objects.filter(name = search_query)
    return render(request, "homepage.html", {"hotels":hotels})

@login_required(login_url= "/login")
def search_flight(request):
    search_query = request.GET["query"]
    flights = Flights.objects.filter(name = search_query)
    return render(request, "flights.html", {"flights":flights})

@login_required(login_url= "/login")
def search_activity(request):
    search_query = request.GET["query"]
    activities = Activities.objects.filter(name = search_query)
    return render(request, "activities.html", {"activities":activities})

@login_required(login_url= "/login")
def search_package(request):
    search_query = request.GET["query"]
    packages = Packages.objects.filter(name = search_query)
    return render(request, "packages.html", {"packages":packages})

@login_required(login_url= "/login")
def search_custom_package(request):
    search_query = request.GET["query"]
    custom_packages = CustomPackages.objects.filter(name = search_query)
    return render(request, "custom_packages.html", {"packages":custom_packages})