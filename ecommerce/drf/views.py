from django.shortcuts import render
from ecommerce.drf.serializer import AllProducts
from ecommerce.inventory import models
from rest_framework import mixins, permissions, viewsets


class AllProductViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,       
    ):
    queryset = models.Product.objects.all()
    serializer_class = AllProducts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"
