from auth_app.models import Flights,UserModelExtended,Hotels,Activities
from django.contrib.auth.models import User
from django.core.exceptions import EmptyResultSet,ObjectDoesNotExist
import logging

class ProductHandler:
    def __init__(self,current_user):
        self.current_user = current_user

    class FlightHandler:
        def __init__(self):
            pass

        def add_flight(self,flight_from,flight_to,price,flight_image,stock):
            try:
                Flights.objects.create(
                user_model_exnteded = self.current_user.usermodelextended
                ,from_dst = flight_from, to_dst = flight_to
                ,product_image_url = flight_image,price = price,stock = stock)

                return True
            except Exception as e:
                print(e)
                return False
            
        def change_flight(self,id,flight_from,flight_to,price,flight_image,stock):
            try:
                flight = Flights.objects.get(id = id)
            
                flight.from_dst = flight_from
                flight.to_dst = flight_to
                flight.product_image_url = flight_image
                flight.price = price
                flight.stock = stock

                flight.save()

                return True
            except Exception as e:
                print(e)
                return False
        
        def get_flight_by_id(self,flight_id):
            try:
                flight = Flights.objects.get(id = flight_id)
                return flight
            except (ObjectDoesNotExist , EmptyResultSet) as e:
                print(e)
                return None
            
        def get_all_flights(self):
            return Flights.objects.all()

        def delete_flight(self,id):
            try:
                flight = Flights.objects.get(id = id)
                flight.delete()

                return True
            except Exception as e:
                print(e)
                return False

    class HotelHandler:
        def __init__(self):
            pass
        
        def add_hotels(self):
            try:
                Hotels.objects.create(
                    
                )
                return True
            except Exception as e:
                print(e)
                return False