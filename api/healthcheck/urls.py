from django.urls import path
from django.urls import include

from healthcheck.views import healthcheck

urlpatterns = [
    path("", healthcheck)
]