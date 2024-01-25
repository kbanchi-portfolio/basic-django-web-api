"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

API_PREFIX = "api/v1/"

urlpatterns = [
    path(f"{API_PREFIX}token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(f"{API_PREFIX}token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(f"{API_PREFIX}admin/", admin.site.urls),
    path(f"{API_PREFIX}healthcheck/", include("healthcheck.urls")),
    path(f"{API_PREFIX}todo/", include("todo.urls")),
    path(f"{API_PREFIX}auths/", include("auths.urls")),
]
