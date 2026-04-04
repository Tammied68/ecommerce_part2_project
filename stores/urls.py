from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_stores, name="list_stores"),
    path("create/", views.create_store, name="create_store"),
    path("<int:store_id>/", views.get_store, name="get_store"),
    path("vendor/<int:vendor_id>/", views.vendor_stores, name="vendor_stores"),
]
