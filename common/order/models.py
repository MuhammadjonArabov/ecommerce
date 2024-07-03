from django.db import models
from common.base import BaseModel
from django.contrib.auth import get_user_model
from common.validators import phone_number_validator
from common.product.models import Product

User = get_user_model()


class Payment(models.IntegerChoices):
    CASH = 1, 'CASH'
    CLICK = 2, 'CLICK'
    PAYME = 3, 'PAYME'


class OrderingStatus(models.IntegerChoices):
    PIN = 1, 'PIN'
    WAITING = 2, 'WAITING'
    ON_WAY = 3, 'ON_WAY',
    DELIVERED = 4, 'DELIVERED'


class Address(BaseModel):
    country = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    village = models.CharField(max_length=120)
    street = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.village}"


class Order(BaseModel):
    comment = models.TextField(null=True, blank=True)
    payment_type = models.IntegerField(choices=Payment.choices, default=Payment.CASH)
    status = models.IntegerField(choices=OrderingStatus.choices, default=OrderingStatus.PIN)
    phone = models.CharField(max_length=17, validators=[phone_number_validator()])
    user = models.ForeignKey(User, related_name='userOrder', on_delete=models.CASCADE, null=True, blank=True)
    address = models.ForeignKey(Address, related_name='addressOrder', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"


class OrderProduct(BaseModel):
    quantity = models.DecimalField(max_digits=50, decimal_places=6, default=0)
    unit_price = models.DecimalField(max_digits=50, decimal_places=6, default=0)
    total_amount = models.DecimalField(max_digits=50, decimal_places=6, default=0)
    order = models.ForeignKey(Order, related_name='orderOrderProduct', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, related_name='productOrderProduct', on_delete=models.CASCADE, null=True,
                                blank=True)

    def __str__(self):
        return f"{self.id}"
