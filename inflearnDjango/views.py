# from rest_framework import viewsets
# from django.contrib.auth.models import User
#
# from blog.models import Post, Comment
# from inflearnDjango.serializers import UserSerializer, PostSerializer, CommentSerializer
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
# ------------------------------------------------
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from blog.models import Post,Comment
from inflearnDjango.serializers import PostListSerializer, PostRetrieveSerializer, CommentSerializer

# Generic view 의 로직
# 1. Data from db
# 2. seriaze //쿼리셋 라인에서 db 로 데이터를 가져와서 serialize 진행. ListAPIView = many= True,
                                                            # RetrieveAPIView = many = False
# 3. response
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer