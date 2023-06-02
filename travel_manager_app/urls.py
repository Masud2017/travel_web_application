from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('product_details/<int:hotel_id>',views.product_details,name = 'product_details'),
    path('add_hotels',views.add_hotel_page,name = 'add_hotels'),
    path('add_new_hotel',views.add_new_hotel,name = 'add_new_hotel'),
    path('delete_hotel/<int:hotel_id>',views.delete_hotel,name = 'delete_hotel'),
    path('flights',views.flights,name = 'flights'),
    path('add_flights',views.add_flights,name = 'add_flights'),
    path('add_new_flight',views.add_new_flight,name = 'add_new_flight'),
    path('flight_details/<int:flight_id>',views.flight_details,name = 'flight_details'),
    path('activities',views.activities,name = 'activities'),
    path('add_activities',views.add_activities,name = 'add_activities'),
    path('add_new_activity',views.add_new_activity,name = 'add_new_activity'),
    path('activity_details/<int:activity_id>',views.activity_details,name = 'activity_details'),

    path('packages',views.packages,name = 'packages'),
    path('package_details/<int:package_id>',views.package_details,name = 'package_details'),
    path('add_packages',views.add_packages,name = 'add_packages'),
    path('add_packages/<int:package_id>',views.add_packages,name = 'add_packages'),

    path('select_hotel_for_package/<int:package_id>/<int:hotel_id>',views.select_hotel_for_package,name = 'select_hotel_for_package'),
    path('select_flight_for_package/<int:package_id>/<int:flight_id>',views.select_flight_for_package,name = 'select_flight_for_package'),
    path('select_activity_for_package/<int:package_id>/<int:activity_id>',views.select_activity_for_package,name = 'select_activity_for_package'),
    path('deselect_activity_for_package/<int:package_id>/<int:activity_id>',views.deselect_activity_for_package,name = 'deselect_activity_for_package'),
    path('save_package/<int:package_id>',views.save_package,name = 'save_package'),

    path('custom_packages',views.custom_packages,name = 'custom_packages'),
    path('add_custom_packages',views.add_custom_packages,name = 'add_custom_packages'),
    path('add_custom_packages/<int:package_id>',views.add_custom_packages,name = 'add_custom_packages'),

    path('save_custom_package/<int:package_id>',views.save_custom_package,name = 'save_custom_package'),

    path('select_hotel_for_custom_package/<int:package_id>/<int:hotel_id>',views.select_hotel_for_custom_package,name = 'select_hotel_for_custom_package'),
    path('select_flight_for_custom_package/<int:package_id>/<int:flight_id>',views.select_flight_for_custom_package,name = 'select_flight_for_custom_package'),
    path('select_activity_for_custom_package/<int:package_id>/<int:activity_id>',views.select_activity_for_custom_package,name = 'select_activity_for_custom_package'),
    path('deselect_activity_for_custom_package/<int:package_id>/<int:activity_id>',views.deselect_activity_for_custom_package,name = 'deselect_activity_for_custom_package'),




]



