from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InternshipRoleViewSet, ApplicationViewSet

router = DefaultRouter()
router.register(r'roles', InternshipRoleViewSet)
router.register(r'applications', ApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]