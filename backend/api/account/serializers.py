from rest_framework import serializers
from apps.account.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "password", "email", "first_name", "last_name", "is_active", "is_staff")

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user
