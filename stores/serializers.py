from rest_framework import serializers
from .models import Store


class StoreSerializer(serializers.ModelSerializer):
    """
    Serializer for Store model instances.
    """

    class Meta:
        model = Store
        fields = ["id", "vendor", "name", "description", "logo"]
        read_only_fields = ["id", "vendor"]