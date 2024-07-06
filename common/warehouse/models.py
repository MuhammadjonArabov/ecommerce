from django.db import models
from django.db.models import Sum

from common.base import BaseModel
from django.contrib.auth import get_user_model

from common.order.models import Order
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


class WarehouseIncomeProduct(BaseModel):
    quantity = models.DecimalField(max_digits=60, decimal_places=6, default=0)
    unit_price = models.DecimalField(max_digits=60, decimal_places=6, default=0)
    total_amount = models.DecimalField(max_digits=60, decimal_places=6, default=0)
    product = models.ForeignKey(Product, related_name='product_income', on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, related_name='warehouse_income', on_delete=models.CASCADE)
    uom = models.ForeignKey(Uom, related_name='uom_income', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"


class Receipt(BaseModel):
    order = models.CharField(max_length=225)
    receipt_data = models.DateField(null=True, blank=True)
    staff = models.ForeignKey(User, related_name='staff_receipt', on_delete=models.CASCADE)

    def __str__(self):
        return self.order


class ReceiptProduct(BaseModel):
    quantity = models.DecimalField(max_digits=60, decimal_places=6, default=0)
    unit_price = models.DecimalField(max_length=60, decimal_places=6, default=0)
    total_amount = models.DecimalField(max_digits=60, decimal_places=6, default=6)
    warehouse = models.ForeignKey(Warehouse, related_name='warehouse_receipt_product', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_receipt_product', on_delete=models.CASCADE)
    receipt = models.ForeignKey(Receipt, related_name='receipt_receipt_product', on_delete=models.CASCADE)
    uom = models.ForeignKey(Uom, related_name='uom_recept_product', on_delete=models.SET_NULL, null=True, blank=True)

    def summ_total(self):
        self.total_amount = self.quantity * self.unit_price
        return self.total_amount

    def save(self, *args, **kwargs):
        self.summ_total()
        super().save(*args, **kwargs)
        self.update_warehouse_product_cost()

    def update_warehouse_product_cost(self):
        warehouse_product = WarehouseProduct.objects.get(warehose=self.warehouse, product=self.product)
        total_amount = ReceiptProduct.objects.filter(warehouse=self.warehouse, product=self.product).aggregate(Sum(
            'total_amount'))['total_amount__sum']
        total_quantity = ReceiptProduct.objects.filter(warehouse=self.warehouse, product=self.product).aggregate(Sum(
            'quantity'))['quantity__sum']

        if total_quantity:
            new_cost_price = total_amount / total_quantity
            warehouse_product.cost_price = new_cost_price
            warehouse_product.save()

    def __str__(self):
        return f"{self.id}"


class WarehouseExpense(BaseModel):
    quantity = models.DecimalField(max_digits=60, decimal_places=6, default=0)
    unit_price = models.DecimalField(max_length=60, decimal_places=6, default=0)
    total_amount = models.DecimalField(max_digits=60, decimal_places=6, default=6)
    warehouse = models.ForeignKey(Warehouse, related_name='warehouse_expense', on_delete=models.SET_NULL, null=True,
                                  blank=True)
    order = models.ForeignKey(Order, related_name='order_expense', on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, related_name='product_expense', on_delete=models.SET_NULL, null=True,
                                blank=True)

    def __str__(self):
        return f"{self.id}"
