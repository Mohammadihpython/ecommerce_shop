import pytest
from ecommerce.drf.serializer import(
    BrandSerializer,
    ProductInventorySerializer,
    ProductAttributeValueSerializer,
    CategorySerializer,
    ProductSerializer,
    
    
)


class TestEcommerceSerializer:
    
    @pytest.mark.api_test
    def test_categorySerializer(self,category_factory):
        category_obj = category_factory.build()
        serializer = CategorySerializer(data=category_obj)
        
        assert serializer.is_valid()
        
    def test_product_serializer(self,product_factory):
        product_obj = product_factory.build()
        serializer = ProductSerializer(data=product_obj)
        
        assert serializer.is_valid()  