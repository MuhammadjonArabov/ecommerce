from django.contrib import admin
from common.uom.models import UomGroup, Uom


@admin.register(UomGroup)
class UomGroup(admin.ModelAdmin):
    pass


@admin.register(Uom)
class Uom(admin.ModelAdmin):
    pass
