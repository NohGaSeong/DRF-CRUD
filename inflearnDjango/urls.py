# from django.urls import path,include
# from rest_framework import routers
# from inflearnDjango.views import UserViewSet, PostViewSet, CommentViewSet
from django.urls import path, include
from inflearnDjango import views
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'post', PostViewSet)
# router.register(r'comment', CommentViewSet)
#
#
# urlpatterns = [
#     path('',include(router.urls)),
# ]

urlpatterns = [
    path('post/', views.PostListAPIView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostRetrieveAPIView.as_view(), name='post-detail'),
    path('post/<int:pk>/like/', views.PostLikeAPIView.as_view(), name='post-like'),
    path('comment/', views.CommentCreateAPIView.as_view(), name='comment-list'),
    path('catetag/', views.CateTagAPIView.as_view(), name='cate-tag')

]