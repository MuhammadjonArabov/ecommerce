from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

from api.category.views import CategoryAPIView, SubCategoryAPIView

router.register(r'category', CategoryAPIView, basename='category')
router.register(r'subcategory', SubCategoryAPIView, basename='subcategory')

urlpatterns = router.urls
