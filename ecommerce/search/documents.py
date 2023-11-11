
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from ecommerce.inventory import models
from elasticsearch_dsl import connections

connections.configure(
    default={'hosts': 'localhost'},
    dev={
        'hosts': ['127.0.0.1:9300'],
        'sniff_on_start': True
    }
)

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


