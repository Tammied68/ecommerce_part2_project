from django.db import models
from stores.models import Store   # <-- correct import
from django.contrib.auth.models import User


class Product(models.Model):
    """
    Represents a product belonging to a specific store.
    """
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="product_images/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
