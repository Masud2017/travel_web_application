from auth_app.models import Flights,UserModelExtended
from django.contrib.auth.models import User

class ProductHandler:
    def __init__(self):
        pass

    def add_flight(flight_from,flight_to,price,flight_image):
        Flights.objects.create()