
from django.shortcuts import render

from django.views import generic
from ecommerce.inventory.models import Category,Product



def home(request):
    return render(request, 'index.html')


class Category(generic.ListView):
    model = Category
    template_name = 'category.html'
    queryset = Category.objects.all()
    context_object_name = 'categories'



class ProductByCategory(generic.View):
    model = Product
    template_name = 'product_by_category.html'
    context_object_name = 'products'
    
    def get(self, request, category):
        products = Product.objects.filter(category__slug=category).values(
            "id","name","description","category__name","product__store_price",)
        
        context = {
            'products': products,
        }
        return render(request, self.template_name, context)
    

class ProductDetail(generic.DetailView):
    model = Product
    template_name = "product_detail.html"
    slug_field = "product"
    slug_url_kwarg = "product"
    
        