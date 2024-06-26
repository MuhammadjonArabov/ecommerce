from tokenize import TokenError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class LoginSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    guid = serializers.CharField(read_only=True)
    phone = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)

    def validate(self, attrs):
        phone = attrs.get('phone')
        password = attrs.get('password')
        user = authenticate(phone=phone, password=password)
        if not user:
            raise serializers.ValidationError('User not fount')
        refresh = RefreshToken.for_user(user)
        return {
            'id': user.id,
            'guid': user.guid,
            'phone': user.phone,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    class Meta:
        model = User
        fields = ['id', 'guid', 'username', 'password', 'refresh', 'access']
        read_only_fields = ['id', 'guid', 'username']


class LogoutSerializers(serializers.Serializer):
    refresh = serializers.CharField()

    def validata(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad token')


class ChangePasswordSerializers(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, required=True)
    conf_password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs.get('new_password') != attrs.get('conf_password'):
            raise serializers.ValidationError("Passwords don't match")
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Incorrect password")
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance


class AdminChangePasswordSerializers(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, required=True)
    conf_password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs.get('new_password') != attrs.get('conf_password'):
            raise serializers.ValidationError("Passwort don't match")
        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance
