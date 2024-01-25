from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def healthcheck(request):
    if request.method == "GET":
        data = {"healthcheck", "ok"}
        return Response(data)