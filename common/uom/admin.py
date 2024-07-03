from django.contrib import admin
from common.order.models import Order, OrderProduct


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    pass
