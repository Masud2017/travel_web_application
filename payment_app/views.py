from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
import stripe
from django.conf import settings
from auth_app.models import Packages,CustomPackages,OrderPackages,OrderCustomPackages
from travel_manager_app import util

def checkout_package(request,package_id):
    stripe.api_key = settings.STRIPE_API_KEY

    package = Packages.objects.get(id = package_id)

    activity_product_json_list = []
 
    hotel = {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": package.hotel.price * 100,
                    "product_data": {
                        "name": package.hotel.name,
                        "images": [package.hotel.product_image_url],
                    },
                },
                "quantity": package.hotel_qty,
            }
    
    activity_product_json_list.append(hotel)

    flight = {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": package.flight.price * 100,
                    "product_data": {
                        "name": package.flight.name,
                        "images": [package.flight.product_image_url],
                    },
                },
                "quantity": package.flight_qty,
            }
    
    activity_product_json_list.append(flight)

    for activity_item in package.activities.all():
        print("name of activity " ,activity_item.name)
        json = {
            "price_data": {
                "currency":"usd",
                "unit_amount": activity_item.price * 100,
                "product_data": {
                    "name": activity_item.name,
                    "images" : [activity_item.product_image_url]
                },
            },
            "quantity":1
        }



        activity_product_json_list.append(json)

    print (activity_product_json_list)

    checkout_session = stripe.checkout.Session.create(
            line_items= activity_product_json_list,
            mode='payment',
            success_url='http://localhost:8000/',
            cancel_url='http://localhost:8000/login',
        )
    
    order = OrderPackages()
    order.user_model_extended = request.user.usermodelextended
    order.is_paid = True
    order.packages = package
    order.payment_id = checkout_session.payment_intent
    order.save()

    util.add_history_order_for_user(request.user.usermodelextended,None,order,"Ordered")

    print("Printing the id of payment : "+checkout_session.payment_intent)
    
    return redirect(checkout_session.url, code=303)


def checkout_custom_package(request,package_id):
    stripe.api_key = settings.STRIPE_API_KEY

    package = CustomPackages.objects.get(id = package_id)

    activity_product_json_list = []
 
    hotel = {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": package.hotel.price * 100,
                    "product_data": {
                        "name": package.hotel.name,
                        "images": [package.hotel.product_image_url],
                    },
                },
                "quantity": package.hotel_qty,
            }
    
    activity_product_json_list.append(hotel)

    flight = {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": package.flight.price * 100,
                    "product_data": {
                        "name": package.flight.name,
                        "images": [package.flight.product_image_url],
                    },
                },
                "quantity": package.flight_qty,
            }
    
    activity_product_json_list.append(flight)

    for activity_item in package.activities.all():
        print("name of activity " ,activity_item.name)
        json = {
            "price_data": {
                "currency":"usd",
                "unit_amount": activity_item.price * 100,
                "product_data": {
                    "name": activity_item.name,
                    "images" : [activity_item.product_image_url]
                },
            },
            "quantity":1
        }



        activity_product_json_list.append(json)

    print (activity_product_json_list)

    checkout_session = stripe.checkout.Session.create(
            line_items= activity_product_json_list,
            mode='payment',
            success_url='http://localhost:8000/',
            cancel_url='http://localhost:8000/login',
        )
    
    order = OrderCustomPackages()
    order.user_model_extended = request.user.usermodelextended
    order.is_paid = True
    order.custom_packages = package
    order.payment_id = checkout_session.payment_intent
    order.save()

    util.add_history_custom_order_for_user(request.user.usermodelextended,None,order,"Ordered")


    print("Printing the id of payment : "+checkout_session.payment_intent)
    
    return redirect(checkout_session.url, code=303)


def refund_package_order(request,order_id):
    order = OrderPackages.objects.get(id = order_id)
    payment_id = order.payment_id
    stripe.api_key = settings.STRIPE_API_KEY
    stripe.Refund.create(payment_intent = payment_id)

    # now re add the qty to the hotel,flight
    hotel = order.packages.hotel
    hotel.stock = hotel.stock + order.packages.hotel_qty
    hotel.save()
    
    flight = order.packages.flight
    flight.stock = flight.stock + order.packages.flight_qty
    flight.save()

    order.is_paid = False
    order.save()

    util.add_history_order_for_agent(request.user.usermodelextended,order.user_model_extended.user,order,"Refunded")
    return HttpResponseRedirect("/")


def refund_custom_package_order(request,order_id):
    order = OrderCustomPackages.objects.get(id = order_id)
    payment_id = order.payment_id
    stripe.api_key = settings.STRIPE_API_KEY
    stripe.Refund.create(payment_intent = payment_id)

    # now re add the qty to the hotel,flight
    hotel = order.custom_packages.hotel
    hotel.stock = hotel.stock + order.custom_packages.hotel_qty
    hotel.save()
    
    flight = order.custom_packages.flight
    flight.stock = flight.stock + order.custom_packages.flight_qty
    flight.save()

    order.is_paid = False
    order.save()

    util.add_history_custom_order_for_agent(request.user.usermodelextended,order.user_model_extended.user,order,"Refunded")
    return HttpResponseRedirect("/")
