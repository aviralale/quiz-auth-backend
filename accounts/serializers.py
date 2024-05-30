# accounts/serializers.py

from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'created_at', 'pfp']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data.get('username', str(uuid.uuid4())),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            pfp=validated_data.get('pfp', 'user_avatar/default.jpg')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.pfp = validated_data.get('pfp', instance.pfp)
        instance.save()
        return instance
