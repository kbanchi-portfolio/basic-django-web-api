from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from todo.views import TodoViewSet
from todo.views import todo_list

router = DefaultRouter()
router.register("todos", TodoViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("list/", todo_list)
]