from api.category.serializer import CategoryCreateSerializers, CategoryListSerializers, SubCategoryCreateSerializers, \
    SubCategoryListSerializers
from common.category.models import Category, SubCategory
from rest_framework import viewsets


class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializers
    lookup_field = 'guid'

    def list(self, request, *args, **kwargs):
        self.serializer_class = CategoryListSerializers
        return super().list(request, *args, **kwargs)


class SubCategoryAPIView(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all().select_related('category')
    serializer_class = SubCategoryCreateSerializers
    lookup_field = 'guid'

    def list(self, request, *args, **kwargs):
        self.serializer_class = SubCategoryListSerializers
        return super().list(request, *args, **kwargs)
