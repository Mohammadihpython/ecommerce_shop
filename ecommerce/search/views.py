

from django.http import HttpResponse
from ecommerce.search.search_serializer import SearchProductInventorySerializer
from ecommerce.search.documents import ProductInventoryDocument
from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView


class SearchProductInventory(APIView, LimitOffsetPagination):
    productinventory_serializer = SearchProductInventorySerializer
    search_document = ProductInventoryDocument
    """
    the multi_match query builds on the
    match query to allow multi-field queries

    Q(): short way of creating a query instance
    fuzziness make a work if has wrong word
    """

    def get(self, request, query):
        try:
            q = Q(
                'multi_match',
                query=query,
                fields=[
                    "product.name"
                ], fuzziness='auto') & Q(
                    'bool',
                    should=[
                        Q('match', is_default=True),
                    ],minimum_should_match =1,

                )
            search=self.search_document.search().query(q)
            response=search.execute()

            results=self.paginate_queryset(response, request, view = self)
            serializer=self.productinventory_serializer(results, many = True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status = 500)
