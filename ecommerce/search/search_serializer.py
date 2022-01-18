from django.db.models.fields.related import ManyToManyField
from ecommerce.inventory.models import ( Product,ProductInventory, )
from rest_framework import serializers

"""
here make a serializer for elasticsearch system 
to integrate DRF and elasticsearch
"""


class SearchProductSerializer(serializers.ModelSerializer):
     class Meta:
        model = Product
        fields = ["name",]
        read_only = True
        editable = False

    
class SearchProductInventorySerializer(serializers.ModelSerializer):
    product = SearchProductSerializer(many=False, read_only=True)
    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "product",
        ]
        read_only = True
    
