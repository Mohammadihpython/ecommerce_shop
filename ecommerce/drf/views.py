from django.shortcuts import get_object_or_404
from ecommerce.drf.serializer import (ProductInventorySerializer,
                                      ProductSerializer,)
from ecommerce.inventory.models import Product, ProductInventory
from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response
import logging

"""
connect to logging config
"""
logger = logging.getLogger("loggers")
class ProductByCategory(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    
):
    """
    API endpoint that returns products by category
    """

    queryset = ProductInventory.objects.all()

    def list(self, request, slug=None,*args,**kwargs):
        """
        show product by category and loging
        """
        message = {
            "message":"user views list of product by category"
        }
        logger.info(message)
        
        queryset = self.queryset.filter(
            product__category__slug=slug,
        ).filter(is_default=True)[:10]
        print(queryset)
        serializer = ProductInventorySerializer(
            queryset, context={"request": request}, many=True
        )
        return Response(serializer.data)


class AllProductViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    """
    API endpoint that returns all products and get one product with slug
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        queryset = Product.objects.filter(slug=slug)[:10]
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)




# class SingleProductViewSet(
#     viewsets.GenericViewSet,
#     mixins.RetrieveModelMixin,
# ):
#     """
#     API endpoint that returns single Item
#     """

#     queryset = ProductInventory.objects.all()
#     serializer_class = ProductInventorySerializer
#     lookup_field = "slug"

#     def retrieve(self, request, slug=None):
#         queryset = ProductInventory.objects.filter(product__slug=slug)
#         serializer = ProductInventorySerializer(queryset, many=True)

#         return Response(serializer.data)


# class SingleProductViewSet(viewsets.ViewSet):
#     """
#     https://www.django-rest-framework.org/api-guide/viewsets/
#     """
#     """
#     here if front end developer set 
#     product attribute it return this product
#     """

#     queryset = ProductInventory.objects.all()
#     serializer_class = ProductInventorySerializer
#     lookup_field = "product__web_id"

#     def list(self, request, id=None):

#         filter_arguments = []
#         q = ProductInventory.objects.all()

#         if request.GET:
#             for value in request.GET.values():
#                 filter_arguments.append(value)
#             queryset = get_object_or_404(q, product__web_id=id)

#         else:
#             queryset = get_object_or_404(q, product__web_id=id, is_default=True)

#         serializer = ProductInventorySerializer(queryset)
#         return Response(serializer.data)



#     # @action(methods=["get"], detail=True)
#     # def singleitem(self, request, pk=None):
#     #     queryset = ProductInventory.objects.filter(pk=pk)
#     #     serializer = SingleProductSerializer(queryset, many=True)
#     #     return Response(serializer.data)
