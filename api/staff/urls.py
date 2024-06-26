from django.urls import path
from api.staff.views import StaffAPIView, StaffDetailAPIView, StaffUpdateAPIView, StaffDeleteAPIView, \
    StaffCreateSerializers

urlpatterns = [
    path('-list/', StaffAPIView.as_view(), name='staff-list'),
    path('-detail/<uuid:guid>/', StaffDetailAPIView.as_view(), name='staff-detail'),
    path('-update/<uuid:guid>/', StaffUpdateAPIView.as_view(), name='staff-update'),
    path('-detail/<uuid:guid>/', StaffDeleteAPIView.as_view(), name='staff-detail'),
    path('-create/', StaffCreateSerializers.as_view(), name='staff-create'),
]
