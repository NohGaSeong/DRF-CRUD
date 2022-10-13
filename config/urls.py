from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# 모델과 필드를 찍고 이걸 json 형태로 바꿔준다고 생각하면됨.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# 쿼리셋을 만드는데,
# 아래있는 코드따라서 쿼리셋 만들어지고, serializer_class 가 UserSerializer 이 되고 json 형태로 보여지게됨.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# /users 호출 = Userviewset 실행
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]