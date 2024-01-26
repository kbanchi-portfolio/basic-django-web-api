from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from auths.models import User
from auths.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer