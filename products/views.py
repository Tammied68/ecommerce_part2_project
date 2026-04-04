from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from products.models import Product
from products.serializers import ProductSerializer
from stores.models import Store


@api_view(["GET", "POST"])
def store_products(request, store_id):
    """
    Retrieve all products for a store or add a new product to that store.
    """
    try:
        store = Store.objects.get(pk=store_id)
    except Store.DoesNotExist:
        return Response(
            {"detail": "Store not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        products = Product.objects.filter(store=store)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if not request.user.is_authenticated:
        return Response(
            {"detail": "Authentication required to add a product."},
            status=status.HTTP_401_UNAUTHORIZED
        )

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        product = serializer.save(store=store)
        return Response(
            ProductSerializer(product).data,
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)