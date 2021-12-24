
from django.shortcuts import render
from django.views import generic
from ecommerce.inventory.models import Category, Product, ProductInventory


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
            "id","slug","name","description","category__name","product__store_price",)
        
        context = {
            'products': products,
        }
        return render(request, self.template_name, context)
    


class ProductDetail(generic.View):
    
      
    
    def get(self, request,slug):
        filter_argument = []
        if self.request.GET:
            for value in request.GET.values():
                filter_argument.append(value)
      
        # slug = self.kwargs.get('slug',None)
        print(slug)
        from django.db.models import Count
        data = ProductInventory.objects.filter(product__slug =slug).filter(
            attribute_values__attribute_value__in=filter_argument).annotate(count_item=Count(
                'attribute_values')).filter(count_item =len(filter_argument)).values(
            "sku","id","product__name","product_inventory__units",)
        print(data)    
        return render(request, "product_detail.html", {"data":data})
