import stripe
# from auth_app import util
import logging
from django.conf import settings

class PaymentService:
    def __init__(self):
        # logging.basicConfig()
        # logging.setLoggerClass("stripe")
        # logging.getLogger('stripe').setLevel(logging.DEBUG)

        token_secret = settings.STRIPE_API_KEY
        
        
        # stripe.PaymentLink.create(
        # line_items=[
        #     {
        #     "price": "card_1NBb4yCahLN2X5RUnDdRMNyc",
        #     "quantity": 1,
        #     },
        # ],
        # )

    def generate_payement_link(self,pacakge_data):
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html'
        )


if __name__ == "__main__":
    service = PaymentService()
    service.generate_payement_link([])