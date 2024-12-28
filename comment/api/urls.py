from django.urls import path, include
from rest_framework.routers import DefaultRouter
from comment.api.views import CommentViewSet

router = DefaultRouter()
router.register("comments", CommentViewSet, basename="comment")

urlpatterns = [
    path("", include(router.urls)),
]
