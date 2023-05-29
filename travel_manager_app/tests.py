from django.test import TestCase
from .services.ProductHandler import ProductHandler
from auth_app.models import UserModelExtended
from django.contrib.auth.models import User

# Create your tests here.

class FlightHandlerTest(TestCase):
    def setUp(self):
        user = User.objects.filter(id = 40).first()
        if user == None:
            print("User is null")
        self.product = ProductHandler(current_user = user)
        self.flight_handler = self.product.FlightHandler(self.product.current_user.usermodelextended)

    def test_stripe_product_creation(self):
        res = self.flight_handler.add_flight(name ="new_one",flight_from="Canada",flight_to="America",price=100,flight_image="",stock = 2,description="hello world this is a description")
        self.assertEqual(res,True)