
from django.shortcuts import render
from django.views import generic
from ecommerce.inventory.models import (Category, Product, ProductInventory,
                                        ProductTypeAttribute)


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
            "id", "slug", "name", "description", "category__name", "product__store_price",)

        context = {
            'products': products,
        }
        return render(request, self.template_name, context)

def product_detail(request, slug):
    # Dynamic Filter
    filter_arguments = []

    if request.GET:
        filter_arguments.extend(iter(request.GET.values()))
        from django.db.models import Count
        from django.contrib.postgres.aggregates import ArrayAgg

        x = ProductInventory.objects.filter(product__slug=slug).filter(attribute_values__attribute_value__in=filter_arguments).annotate(num_tags=Count('attribute_values')).filter(num_tags=len(filter_arguments)).values(
        "id", "sku", "product__name", "store_price", "product_inventory__units").annotate(field_a=ArrayAgg("attribute_values__attribute_value")).get()
    else:

        from django.contrib.postgres.aggregates import ArrayAgg

        x = ProductInventory.objects.filter(product__slug=slug).filter(is_default=True).values(
        "id", "sku", "product__name", "store_price", "product_inventory__units").annotate(field_a=ArrayAgg("attribute_values__attribute_value")).get()


    y = ProductInventory.objects.filter(product__slug=slug).distinct().values(
    "attribute_values__product_attribute__name", "attribute_values__attribute_value")

    z = ProductTypeAttribute.objects.filter(product_type__product_type__product__slug=slug).distinct().values("product_attribute__name")

    return render(request, "product_detail.html", {"x": x, "filter": y, "z": z})
