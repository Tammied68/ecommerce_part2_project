from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render
from django.contrib.auth.models import User
from stores.models import Store
from stores.serializers import StoreSerializer


"""
    Landing page view for the application.
    """


def home(request):
    return render(request, "home.html")


@api_view(["GET"])
def list_stores(request):
    """
    Return a list of all stores.
    """
    stores = Store.objects.all()
    serializer = StoreSerializer(stores, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_store(request, store_id):
    """
    Return a single store by ID.
    """
    try:
        store = Store.objects.get(pk=store_id)
    except Store.DoesNotExist:
        return Response(
            {"detail": "Store not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = StoreSerializer(store)
    return Response(serializer.data)


@api_view(["GET"])
def vendor_stores(request, vendor_id):
    """
    Return all stores belonging to a specific vendor.
    """
    try:
        User.objects.get(pk=vendor_id)
    except User.DoesNotExist:
        return Response(
            {"detail": "Vendor not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    stores = Store.objects.filter(vendor_id=vendor_id)
    serializer = StoreSerializer(stores, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_store(request):
    """
    Create a new store for the authenticated vendor.
    """
    if not request.user.is_authenticated:
        return Response(
            {"detail": "Authentication required to create a store."},
            status=status.HTTP_401_UNAUTHORIZED
        )

    serializer = StoreSerializer(data=request.data)
    if serializer.is_valid():
        store = serializer.save(vendor=request.user)
        return Response(
            StoreSerializer(store).data,
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)