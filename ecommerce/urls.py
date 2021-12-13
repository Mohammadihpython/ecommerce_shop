
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include("ecommerce.demo.urls", namespace="demo")),
]
