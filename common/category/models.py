from django.db import models
from common.base import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='categoryImages', null=True, blank=True)

    def __str__(self):
        return self.title


class SubCategory(BaseModel):
    title = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='categoryImages', null=True, blank=True)
    category = models.ForeignKey(Category, related_name='categorySubCategory', on_delete=models.CASCADE, null=True,
                                 blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"
