from django.urls import path
from ecommerce.demo import views
from ecommerce.demo.views import Category,ProductByCategory,product_detail




app_name="demo"
urlpatterns = [
    path('',views.home, name="home"),
  
    path('categories/',Category.as_view(), name="categories"),
    path('product-by-category/<slug:category>/',ProductByCategory.as_view(), name="product_by_category"),
    path('<slug:slug>/',product_detail, name="product-detail"),
]
