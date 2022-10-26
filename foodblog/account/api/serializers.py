from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        )

        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):        
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        serializers = UserDetailSerializer(user)
        data.update(serializers.data)
        return data