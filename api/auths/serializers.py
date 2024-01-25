from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from auths.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def validate_password(self, value:str) -> str:
        return make_password(value)