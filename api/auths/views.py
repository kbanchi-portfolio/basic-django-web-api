from django.shortcuts import render
from rest_framework import viewsets
from auths.models import User
from auths.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer