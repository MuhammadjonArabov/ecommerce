from django.db import models, transaction
from common.base import BaseModel
from config.settings.base import env
from common.category.models import Category
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(BaseModel):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField()
    quantity = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey(Category, related_name='categoryProduct', on_delete=models.CASCADE,
                                 blank=True, null=True)

    def __str__(self):
        return self.title


class ProductImage(BaseModel):
    photo = models.ImageField(upload_to='productImage', null=True, blank=True)
    isMain = models.BooleanField(default=False)
    product = models.ForeignKey(Product, related_name='productProductImage', on_delete=models.CASCADE,
                                null=True, blank=True)

    @product
    def imageURL(self):
        if self.product.photo:
            return env.str('BASE_URL') + self.product.photo.url
        return ""

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        if self.isMain:
            while transaction.atomic():
                ProductImage.objects.filter(product=self.product, isMain=True).update(isMain=False)
        super().save(*args, **kwargs)


class Comment(BaseModel):
    user = models.ForeignKey(User, related_name='userComment', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, related_name='productComment', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()

    def __str__(self):
        return {self.id}

    class Meat:
        ordering = ['-created_at']
