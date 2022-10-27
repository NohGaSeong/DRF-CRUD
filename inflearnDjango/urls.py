from django.urls import path,include
from rest_framework import routers
from inflearnDjango.views import UserViewSet, PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)


urlpatterns = [
    path('',include(router.urls)),
]