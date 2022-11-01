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
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, GenericAPIView
from blog.models import Post,Comment, Category, Tag
from inflearnDjango.serializers import PostListSerializer, PostRetrieveSerializer, CommentSerializer, \
    PostLikeSerializer, CategorySerializer, CateTagSerializer, PostSerializerDetail
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
# Generic view 의 로직
# 1. Data from db
# 2. seriaze //쿼리셋 라인에서 db 로 데이터를 가져와서 serialize 진행. ListAPIView = many= True,
                                                            # RetrieveAPIView = many = False
# 3. response
# class PostListAPIView(ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostListSerializer

def get_prev_next(instance):
    try:
        prev = instance.get_previous_by_update_dt()
    except instance.DoesNotExist:
        prev = None

    try:
        next_ = instance.get_next_by_update_dt()
    except instance.DoesNotExist:
        next_ = None

    return prev, next_



class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerDetail

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        preInstance = instance.get_previous_by_update_dt()
        nextInstance = instance.get_next_by_update_dt()
        commentList = instance.comment_set.all()
        data = {
            'post':instance,
            'prePost':preInstance,
            'nextPost':nextInstance,
            'commentList':commentList,
        }
        serializer = self.get_serializer(instance=data)
        return Response(serializer.data)

    def get_serializer_context(self):
        return {
            'request':None,
            'format': self.format_kwarg,
            'view':self
        }

class PostLikeAPIView(GenericAPIView):
    queryset = Post.objects.all()
    # serializer_class = PostLikeSerializer

    # PATCH method
    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     # data = instance.like + 1
    #     data = {'like': instance.like + 1}
    #     serializer = self.get_serializer(instance, data=data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #
    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}
    #
    #     # return Response(serializer.data)
    #     return Response(data['like'])

    # GetMethod
    queryset = Post.objects.all()
    # serializer_class = PostLikeSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.like += 1
        instance.save()
        return Response(instance.like)

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CateTagAPIView(APIView ):
    def get(self, request, *args, **kwargs):
        cateList = Category.objects.all()
        tagList = Tag.objects.all()
        data = {
            'cateList': cateList,
            'tagList': tagList,
        }

        serializer = CateTagSerializer(instance=data)

        return Response(serializer.data)

class PostPageNumberPagination(PageNumberPagination):
    page_size = 3

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('postList', data),
            ('pageCnt', self.page.paginator.num_pages),
            ('curPage', self.page.number),
        ]))

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostPageNumberPagination

    def get_serializer_context(self):
        return {
            'request':None,
            'format':self.format_kwarg,
            'view':self
        }

