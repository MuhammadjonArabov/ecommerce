from drf_base64.fields import Base64ImageField
from rest_framework import serializers
from config.settings.base import env
from common.product.models import Product, ProductImage


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'guid', 'title', 'price', 'description', 'quantity', 'category']


class ProductListSerializer(serializers.ModelSerializer):
    productImage = serializers.SerializerMethodField()


class ProductShortSerializer(serializers.ModelSerializer):
    warehouse_product_quantity = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()

    def get_warehouse_product_quantity(self, obj):
        warehouses = self.context['warehouses']
        data = {}
        for warehouse in warehouses:
            matching_products = [k for k in obj.productWarehouseProduct.all() if k.warehouse.id == warehouse.id]
            data[warehouse.id] = sum(k.quantity for k in matching_products) if matching_products else 0
        return data

    def get_total_quantity(self, obj):
        if hasattr(obj, 'total_quantity'):
            return obj.total_quantity or 0
        return 0

    class Meta:
        model = Product
        fields = ['id', 'guid', 'title', 'total_quantity', 'warehouse_product_quantity']


class ProductImageListSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    def get_photo(self, product):
        if product.photo:
            return env.str('BASE_URL') + product.photo.url
        return ''

    class Meta:
        model = ProductImage
        fields = ['id', 'guid', 'photo', 'isMain']


class ProductImageCreateSerializer(serializers.ModelSerializer):
    photo = Base64ImageField(required=True)
    id = serializers.IntegerField(read_only=True)
    guid = serializers.CharField(read_only=True)
    isMain = serializers.BooleanField(required=True)

    class Meta:
        model = ProductImage
        fields = ['id', 'guid', 'photo', 'isMain', 'product']
