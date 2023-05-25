import stripe
from auth_app import util
import logging

class PaymentService:
    def __init__(self):
        logging.basicConfig()
        logging.setLoggerClass("stripe")
        logging.getLogger('stripe').setLevel(logging.DEBUG)
