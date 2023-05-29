from auth_app.models import Flights,UserModelExtended,Hotels,Activities
from django.contrib.auth.models import User
from django.core.exceptions import EmptyResultSet,ObjectDoesNotExist
import stripe
from django.conf import settings

class ProductHandler:
    def __init__(self,current_user):
        self.current_user = current_user
        print("environment variable printin : ",settings.STRIPE_API_KEY)

    class FlightHandler:
        def __init__(self,current_user):
            self.current_user = current_user
            stripe.api_key = "sk_test_PoBT6YH9zQk0e1CmaBBvwE9T00DzILwK1R"
            

        def add_flight(self,name,flight_from,flight_to,price,flight_image,stock,description):
            try:
                product = stripe.Product.create(
                    name = "Flight name : "+name +' | from : '+flight_from + " | to : "+flight_to
                )

                price = stripe.Price.create(
                    unit_amount=2000,
                    currency="usd",
                    recurring={"interval": "month"},
                    product=product.id,
                )
                
                Flights.objects.create(
                    user_model_exnteded = self.current_user.usermodelextended
                    ,name = name
                    ,from_dst = flight_from, to_dst = flight_to
                    ,product_image_url = flight_image,price = price,stock = stock
                    ,price_id = price.id
                    ,product_id = product.id,description = description)

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
        
        def add_hotel(self,count,size,description,image,price,stock):
            try:
                Hotels.objects.create(
                    user_model_extended = self.current_user,
                    room_count = count,
                    room_size = size,
                    description = description,
                    product_image_url = image,
                    price = price,
                    stock = stock
                )

                return True
            except Exception as e:
                print(e)
                return False
            
        def change_hotel(self,id,count,size,description,image,price,stock):
            try:
                hotel = Hotels.objects.get(id = id)
            
                hotel.room_count = count
                hotel.room_size = size
                hotel.product_image_url = image
                hotel.description = description
                hotel.price = price
                hotel.stock = stock

                hotel.save()

                return True
            except Exception as e:
                print(e)
                return False
        
        def get_hotel_by_id(self,hotel_id):
            try:
                hotel = Hotels.objects.get(id = hotel_id)
                return hotel
            except (ObjectDoesNotExist , EmptyResultSet) as e:
                print(e)
                return None
            
        def get_all_hotels(self):
            return Hotels.objects.all()

        def delete_hotel(self,id):
            try:
                hotel = Hotels.objects.get(id = id)
                hotel.delete()

                return True
            except Exception as e:
                print(e)
                return False
            
    class ActivityHandler:
        def __init__(self):
            pass

        def add_activity(self,name,description,price,image):
            try:
                Activities.objects.create(
                    user_model_extended = self.current_user,
                    name = name,
                    description = description,
                    product_image_url = image,
                    price = price,
                )

                return True
            except Exception as e:
                print(e)
                return False
            
        def change_activity(self,id,name,description,price,image):
            try:
                activity = Activities.objects.get(id = id)

                activity.name = name            
                activity.product_image_url = image
                activity.description = description
                activity.price = price

                activity.save()

                return True
            except Exception as e:
                print(e)
                return False
        
        def get_activity_by_id(self,hotel_id):
            try:
                activity = Activities.objects.get(id = hotel_id)
                return activity
            except (ObjectDoesNotExist , EmptyResultSet) as e:
                print(e)
                return None
            
        def get_all_acitivities(self):
            return Activities.objects.all()

        def delete_activity(self,id):
            try:
                activity = Activities.objects.get(id = id)
                activity.delete()

                return True
            except Exception as e:
                print(e)
                return False
            

if __name__ == "__main__":
    handler = ProductHandler.FlightHandler()
    handler.add_flight(name= "Test flight", flight_from= "Canada",flight_to= "America",price=100,flight_image="",stock=1)
