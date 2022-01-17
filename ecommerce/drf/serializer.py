from dataclasses import field

from ecommerce.inventory import models
from rest_framework import serializers


class AllProducts(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"
