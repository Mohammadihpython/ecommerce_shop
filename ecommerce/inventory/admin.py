from django.contrib import admin
from ecommerce.inventory.models import (Brand, Category, Media, Product,
                                        ProductAttribute,
                                        ProductAttributeValue,
                                        ProductAttributeValues,
                                        ProductInventory, ProductType, Stock)

admin.site.register(Brand)

admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    filter_horizontal = ("category",)


admin.site.register(ProductType)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
admin.site.register(ProductInventory)
admin.site.register(Media)
admin.site.register(Stock)
admin.site.register(ProductAttributeValues)
