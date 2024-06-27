from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from api.staff.serializer import StaffSerializers, StaffDetailSerializers, StaffCreateSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

User = get_user_model()


class StaffCreateSerializers(CreateAPIView):
    serializer_class = StaffCreateSerializer


class StaffAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = StaffSerializers
    #permission_classes = (IsAuthenticated,)


class StaffDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = StaffDetailSerializers
    lookup_field = 'guid'


class StaffUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = StaffCreateSerializers
    lookup_field = 'guid'
    permission_classes = (IsAuthenticated,)


class StaffDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = StaffCreateSerializers
    lookup_field = 'guid'
    permission_classes = (IsAuthenticated,)


