import pytest
from ecommerce.tests.fixture import api_client, db_fixture_setup
from rest_framework import status

class TestInventoryApi():
    
    endpoint = "/products/"
    def test_get_product_inventory(
            self,
            db,
            db_fixture_setup,
            api_client,):
        """
        Test get all product inventory
        """
        response = api_client.get("/products/")
        
        assert response.status_code == status.HTTP_200_OK
    
    def test_get_product_by_category(
         self,
            db,
            db_fixture_setup,
            api_client,
    ):
        """
        Test get all product with specific category
        """
        response = api_client.get("/category/baseball/")
        
        assert response.status_code == status.HTTP_200_OK
       
        