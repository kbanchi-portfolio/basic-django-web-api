from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


@api_view(["GET"])
@permission_classes((AllowAny, ))
def healthcheck(request):
    if request.method == "GET":
        data = {"healthcheck": "ok"}
        return Response(data)