from django.contrib import admin
from ecommerce.inventory.models import (Brand, Category, Media, Product,
                                        ProductAttribute,
                                        ProductAttributeValue,
                                        ProductAttributeValues,
                                        ProductInventory, ProductType, Stock)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'parent', 'slug')


admin.site.register(Brand)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    filter_horizontal = ("category",)


admin.site.register(ProductType)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
admin.site.register(ProductInventory)
admin.site.register(Media)
admin.site.register(Stock)
admin.site.register(ProductAttributeValues)
