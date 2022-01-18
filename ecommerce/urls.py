
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from ecommerce.drf import views

from ecommerce.search.views import SearchProductInventory
router = routers.DefaultRouter()
router.register(
    r"category/(?P<slug>[^/.]+)",
    views.ProductByCategory,
    basename="productbycategory",
)
"""This api get all products
   if get slug it return variant of product 
"""
router.register(
    r"products",
    views.AllProductViewSet,
    basename="allproducts"
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include("ecommerce.demo.urls", namespace="demo")),
    path('', include(router.urls)),
    path('search/<str:query>/',SearchProductInventory.as_view()),
    
]
