from auth_app.models import Flights,UserModelExtended
from django.contrib.auth.models import User

class ProductHandler:
    def __init__(self,current_user):
        self.current_user = current_user

    def add_flight(self,flight_from,flight_to,price,flight_image):
        Flights.objects.create(user_model_exnteded = self.current_user.usermodelextended,from_dst = flight_from, to_dst = flight_to,product_image_url = flight_image,price = price)