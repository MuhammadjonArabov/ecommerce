from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LoginAPIView, LogoutAPIVIew, ChangePasswordAPIView
urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='auth-login'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutAPIVIew.as_view(), name='logout'),
    path('change-password/<uuid:guid>/', ChangePasswordAPIView.as_view(), name='change-password'),
]
