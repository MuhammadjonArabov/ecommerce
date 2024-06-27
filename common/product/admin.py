from django.contrib import admin
from common.product.models import Product, ProductImage


@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category']
    list_filter = ['category']
    exclude = ['created_at', 'updated_at']

    save_on_top = True


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass
