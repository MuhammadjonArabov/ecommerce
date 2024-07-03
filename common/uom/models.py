from django.db import models
from common.base import BaseModel


class UomGroup(BaseModel):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class Uom(BaseModel):
    title = models.CharField(max_length=60)
    base_quantity = models.DecimalField(max_digits=50, decimal_places=6, default=0)
    quantity = models.DecimalField(max_digits=50, decimal_places=6, default=0)
    uomGroup = models.ForeignKey(UomGroup, related_name='uomGroupUom', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
