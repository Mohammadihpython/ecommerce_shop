
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from ecommerce.drf import views

router = routers.DefaultRouter()
router.register(
    r"category/(?P<slug>[^/.]+)",
    views.ProductByCategory,
    basename="productbycategory",
)
router.register(
    r"api", views.AllProductViewSet,basename="allproducts"
)
router.register(
    r"product/(?P<slug>[^/.]+)", views.ProductInventoryViewset,basename="products"
)
router.register(
    r"product/(?P<product__web_id>[^/.]+)", views.SingleProductViewSet,basename="singleproduct"
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include("ecommerce.demo.urls", namespace="demo")),
    path('', include(router.urls)),
]
