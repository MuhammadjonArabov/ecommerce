from django.db import models
from common.base import BaseModel
from django.contrib.auth import get_user_model
from common.product.models import Product

User = get_user_model()


class Cart(BaseModel):
    user = models.ForeignKey(User, related_name='userCart', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"


class CartProduct(BaseModel):
    cart = models.ForeignKey(Cart, related_name='cartCartProduct', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, related_name='productCartProduct', on_delete=models.CASCADE, null=True,
                                blank=True)
    quantity = models.DecimalField(max_digits=20, decimal_places=6, default=0)

    def __str__(self):
        return f"{self.id}"

    @property
    def total_price(self):
        return self.product.price * self.quantity


class Wishlist(BaseModel):
    user = models.ForeignKey(User, related_name='userWishlist', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"


class WishlistProduct(BaseModel):
    wishlist = models.ForeignKey(Wishlist, related_name='wishlistWishlistProduct', on_delete=models.CASCADE, null=True,
                                 blank=True)
    product = models.ForeignKey(Product, related_name='productWishlistProduct', on_delete=models.CASCADE, null=True,
                                blank=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        unique_together = (('user', 'product'),)
        verbose_name = "Wishlist Product"
        verbose_name_plural = "Wishlist Products"
