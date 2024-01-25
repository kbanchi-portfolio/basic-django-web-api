from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from auths.views import UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]