"""
URL configuration for the Products API.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("<int:store_id>/products/", views.store_products, name="store_products"),
]
