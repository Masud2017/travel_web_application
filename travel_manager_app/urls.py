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

]

