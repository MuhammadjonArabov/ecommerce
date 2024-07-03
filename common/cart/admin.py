from django.contrib import admin
from common.cart.models import Cart, CartProduct, Wishlist, WishlistProduct


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    pass


@admin.register(WishlistProduct)
class WishlistProductAdmin(admin.ModelAdmin):
    pass
