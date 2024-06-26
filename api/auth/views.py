from rest_framework.views import APIView

from api.auth.serializer import LoginSerializers, LogoutSerializers, ChangePasswordSerializers, \
    AdminChangePasswordSerializers
from rest_framework.generics import CreateAPIView, GenericAPIView, UpdateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginAPIView(CreateAPIView):
    serializer_class = LoginSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(uisername=serializer.data.get('username')).first()
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'id': user.id,
                'guid': user.guid,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({"error": "Invalid credentials"})
        return super().create(request, *args, **kwargs)


class LogoutAPIVIew(GenericAPIView):
    serializer_class = LogoutSerializers
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(rais_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChangePasswordAPIView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'guid'

    def get_serializer_class(self):
        if self.request.user.is_superuser or self.response.user.is_staff:
            return AdminChangePasswordSerializers
        return ChangePasswordSerializers
