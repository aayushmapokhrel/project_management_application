from django.urls import path, include
from rest_framework.routers import DefaultRouter
from project.api.views import ProjectViewSet

router = DefaultRouter()
router.register("projects", ProjectViewSet, basename="Project")

urlpatterns = [
    path("", include(router.urls)),
]
