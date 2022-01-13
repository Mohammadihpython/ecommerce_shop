from dataclasses import field
from django_elasticsearch_dsl import Document,fields
from django_elasticsearch_dsl.registries import registry

from .models import ProductInventory


@registry.register_document
class ProductInventoryDocument(Document):
    """
    for get foreignkey field data
    """
    product =fields.ObjectField(
        properties={
            "name":fields.TextField()
        }
    )
    
    """
    foreignkey field data to stock model product_inventory is a related_name in stock model
    """
    
    product_inventory =fields.ObjectField(
        properties={
            "units":fields.IntegerField()
        }
    )
    
    
    
    
    """
    here we make name for index that have our document
    """
    class Index:
        name = "productinventory"
    """
    here we access django model and say with fields we want
    """
    class Django:
        model = ProductInventory

        fields = ["id", "sku"]

"""
 how get information from elasticsearch?
 first with api

curl -X GET "localhost:9200/_search?pretty" -H 'Content-type:application/json' -d'
{
    "query": {
        "bool": {
            "must": [
             {"match": {"sku": "7633969397"}}
            ]
        }
    }
}
'


secend 

ProductInventoryDocument.search().filter("term",name="bamboo nadya open toe synthetithong sandal")

*for get foreignkey field data  make query like this
*x = ProductInventoryDocument.search().query("match", product__name="bamboo nadya open toe synthetithong sandal")
')
curl -X GET "localhost:92--/productinventory/_doc/1?pretty"
"""