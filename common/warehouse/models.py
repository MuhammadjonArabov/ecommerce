from django.db import models
from common.base import BaseModel
from django.contrib.auth import get_user_model
from common.product.models import Product
from common.uom.models import Uom

User = get_user_model()


class Warehouse(BaseModel):
    title = models.CharField(max_length=255)
    staff = models.ForeignKey(User, related_name='staff_warehouse', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class WarehouseProduct(BaseModel):
    quantity = models.DecimalField(max_digits=60, decimal_places=6, default=0)
    cost_price = models.DecimalField(max_digits=60, decimal_places=6, default=0)
    warehouse = models.ForeignKey(Warehouse, related_name='warehouse_warehouse_product', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_warehouse_product', on_delete=models.CASCADE)
    uom = models.ForeignKey(Uom, related_name='uom_warehouse_product', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"
