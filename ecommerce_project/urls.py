"""
Main URL configuration for the ecommerce project.
Routes API endpoints for stores and products.
"""

from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    # Root landing page
    path("", home, name="home"),

    # Admin
    path("admin/", admin.site.urls),

    # App routes
    path("stores/", include("stores.urls")),
    path("products/", include("products.urls")),
]
