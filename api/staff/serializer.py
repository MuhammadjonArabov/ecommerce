from rest_framework import serializers
from django.contrib.auth import get_user_model, hashers

User = get_user_model()


class StaffCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input': 'password'}, max_length=8)

    def validate_password(self, value):
        if value is None or len(value) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters')
        password = hashers.make_password(value)
        return password

    class Meta:
        model = User
        fields = ['id', 'guid', 'phone', 'name', 'password']


class StaffSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'guid', 'name', 'phone']


class StaffDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
