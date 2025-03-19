from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserAccessRoleViewSet

router = DefaultRouter()
router.register(r'roles', UserAccessRoleViewSet, basename='role')

urlpatterns = [
    path('', include(router.urls)),
]
