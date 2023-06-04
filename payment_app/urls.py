from django.urls import path
from . import views

urlpatterns = [
    path("checkout_package/<int:package_id>", views.checkout_package , name = "checkout_package"),
    path("checkout_custom_package/<int:package_id>", views.checkout_custom_package , name = "checkout_custom_package"),

    path("refund_package_order/<int:order_id>", views.refund_package_order , name = "refund_package_order"),
    path("refund_custom_package_order/<int:order_id>", views.refund_custom_package_order , name = "refund_custom_package_order"),
]
