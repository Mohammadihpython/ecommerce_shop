
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


# class ProductDetail(generic.View):

#     def get(self, request, slug):
#         filter_argument = []
#         if self.request.GET:
#             for value in request.GET.values():
#                 filter_argument.append(value)

#         # slug = self.kwargs.get('slug',None)
#         print(slug)
#         from django.contrib.postgres.aggregates import ArrayAgg
#         from django.db.models import Count
       
#         data = ProductInventory.objects.filter(product__slug=slug).filter(
#             attribute_values__attribute_value__in=filter_argument).annotate(count_item=Count(
#                 'attribute_values')).filter(count_item=len(filter_argument)).values(
#             "sku", "id", "product__name", "product_inventory__units",).annotate(field_a=ArrayAgg("attribute_values__attribute_value")).get()
       
       
       
      
#         y = ProductInventory.objects.filter(product__slug=slug).distinct().values(
#             "attribute_values__product_attribute__name", "attribute_values__attribute_value")
#         """
#          whats z query?
#            * first we connect to ProductTypeAttribute then we connect to producttype model
#            * then with related name we connect to inventory
#             model here we connet to product model and get product with slug =slug then
#             we get this product type attribute!
#         """
#         z = ProductTypeAttribute.objects.filter(
#             product_type__product_type__product__slug=slug).distinct().values("product_attribute__name")
#         return render(request, "product_detail.html", {"data": data, "z": z, "filter": y})

#     def post(self, request, slug):
#         from django.contrib.postgres.aggregates import ArrayAgg

#         x = ProductInventory.objects.filter(product__slug=slug).filter(is_default=True).values(
#             "sku", "id", "product__name", "product_inventory__units",).annotate(field_a=ArrayAgg("attribute_values__attribute_value")).get()

#         return render(request, "product_detail.html", {"x": x, })


# def product_by_category(request, category):
    
#     # x = models.Product.objects.filter(category__name="fashion")
#     # print(models.Product.objects.filter(category__name="fashion").explain(verbose=True, analyze=True))

#     y = models.Product.objects.filter(category__name=category).filter(product__is_default=True).values(
#         "id", "name", "slug", "created_at", "category__name", "product__store_price"
#     )

#     # data = serializers.serialize("json", x, indent=4)

#     return render(request, "product_by_category.html", {"data": y})


def product_detail(request, slug):

    # x = models.Product.objects.filter(slug=slug)

    # x = models.ProductInventory.objects.filter(product__slug=slug).values("id", "product__name", "store_price", "is_default", "attribute_values__attribute_value")

    # Using chained filters approach
    # x = models.ProductInventory.objects.filter(product__slug=slug).filter(attribute_values__attribute_value="red").filter(attribute_values__attribute_value=5).select_related('product')

    # from django.db.models import Count
    # filter_arguments = [5, "red"]
    # x = models.ProductInventory.objects.filter(product__slug=slug).filter(attribute_values__attribute_value__in=filter_arguments).annotate(num_tags=Count('attribute_values')).filter(num_tags=len(filter_arguments))


    # Dynamic Filter
    filter_arguments = []

    if request.GET:
        for value in request.GET.values():
            filter_arguments.append(value)

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
