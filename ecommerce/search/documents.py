from dataclasses import field
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from ecommerce.inventory import models


@registry.register_document
class ProductInventoryDocument(Document):
    product =fields.ObjectField(
        properties= {
            "name": fields.TextField()
        }
    )
    class Index:
        name ="productinventory"
    
    class Django:
        model =models.ProductInventory
        
        """
        this fields must same with fields in your serializer
        """
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
        ]
            

