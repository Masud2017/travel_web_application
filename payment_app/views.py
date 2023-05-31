from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
import stripe
from django.conf import settings

def checkout(request):
    stripe.api_key = "sk_test_PoBT6YH9zQk0e1CmaBBvwE9T00DzILwK1R"
    print(settings.STRIPE_API_KEY)

    checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": 2000,
                        "product_data": {
                            "name": "test_from_code_product",
                            "images": ["https://images.pexels.com/photos/164595/pexels-photo-164595.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"],
                        },
                    },
                    "quantity": 1,
                },
                 {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": 2000,
                        "product_data": {
                            "name": "test_from_code_product",
                            "images": ["https://images.pexels.com/photos/164595/pexels-photo-164595.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"],
                        },
                    },
                    "quantity": 2,
                }
            ],
            mode='payment',
            success_url='http://localhost:8000/',
            cancel_url='http://localhost:8000/login',
        )
    
    print("Printing the id of payment : "+checkout_session.payment_intent)
    
    return redirect(checkout_session.url, code=303)
