from common.category.models import Category, SubCategory
from drf_base64.fields import Base64ImageField
from rest_framework import serializers
from config.settings.base import env


class CategoryCreateSerializers(serializers.ModelSerializer):
    photo = Base64ImageField(required=True)

    class Meta:
        model = Category
        fields = ['id', 'guid', 'photo', 'title']


class CategoryListSerializers(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    def get_photo(self, obj):
        if obj.photo:
            return f"{env.str('BASE_URL')}{obj.photo.url}"
        return ""

    class Meta:
        model = Category
        fields = ['id', 'guid', 'photo', 'title']


class SubCategoryCreateSerializers(serializers.ModelSerializer):
    photo = Base64ImageField()

    def validate(self, attrs):
        category = attrs.get('category')

        if isinstance(category, Category):
            category_id = category.id
        else:
            category_id = category

        if not Category.objects.filter(id=category_id).exists():
            raise serializers.ValidationError({"category": "Category should be chosen"})
        return attrs

    class Meta:
        model = SubCategory
        fields = ['id', 'guid', 'category', 'title', 'photo']


class SubCategoryListSerializers(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    category = CategoryListSerializers()

    def get_photo(self, obj):
        if obj.photo:
            return f"{env.str('BASE_URL')}{obj.photo.url}"
        return ""

    class Meta:
        model = SubCategory
        fields = ['id', 'guid', 'photo', 'title', 'category']
