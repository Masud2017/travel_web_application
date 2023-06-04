from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('product_details/<int:hotel_id>',views.product_details,name = 'product_details'),
    path('add_hotels',views.add_hotel_page,name = 'add_hotels'),
    path('add_new_hotel',views.add_new_hotel,name = 'add_new_hotel'),
    path('delete_hotel/<int:hotel_id>',views.delete_hotel,name = 'delete_hotel'),
    path('delete_flight/<int:flight_id>',views.delete_hotel,name = 'delete_flight'),
    path('delete_package/<int:package_id>',views.delete_package,name = 'delete_package'),
    path('delete_custom_package/<int:package_id>',views.delete_custom_package,name = 'delete_custom_package'),
    path('delete_activity/<int:activity_id>',views.delete_activity,name = 'delete_activity'),



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
    path('custom_package_details/<int:package_id>',views.custom_packages_details,name = 'custom_package_details'),
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


    path('order_package/<int:package_id>',views.order_package,name = 'order_package'),
    path('order_custom_package/<int:package_id>',views.order_custom_package,name = 'order_custom_package'),

    path('my_orders',views.myorders,name = 'my_orders'),

    path('histories',views.histories,name = 'histories'),
    path('add_history/<slug:status>/<int:order_id>/<int:other_user_id>',views.add_history,name = 'add_history'),
    path('add_history/<slug:status>/<int:order_id>',views.add_history,name = 'add_history'),
    path('add_custom_history/<str:status>/<int:order_id>/<int:other_user_id>',views.add_custom_history,name = 'add_custom_history'),
    path('add_custom_history/<str:status>/<int:order_id>',views.add_custom_history,name = 'add_custom_history'),


    path('user_contacts',views.user_contacts,name = 'user_contacts'),
    path('revenue',views.revenue,name = 'revenue'),

    path('search_hotel',views.search_hotel,name = 'search_hotel'),
    path('search_flight',views.search_flight,name = 'search_flight'),
    path('search_activity',views.search_activity,name = 'search_activity'),
    path('search_package',views.search_package,name = 'search_package'),
    path('search_custom_package',views.search_custom_package,name = 'search_custom_package'),


    path('edit_hotel/<int:hotel_id>',views.edit_hotel,name = 'edit_hotel'),
    path('edit_flight/<int:flight_id>',views.edit_flight,name = 'edit_flight'),
    path('edit_activity/<int:activity_id>',views.edit_activity,name = 'edit_activity'),


    path('edit_hotel_with_data/<int:hotel_id>',views.edit_hotel_with_data,name = 'edit_hotel_with_data'),
    path('edit_flight_with_data/<int:flight_id>',views.edit_flight_with_data,name = 'edit_flight_with_data'),
    path('edit_activity_with_data/<int:activity_id>',views.edit_activity_with_data,name = 'edit_activity_with_data'),
]



