from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User

# ViewSet의 장점?
# - 반복되는 로직을 하나의 클래스로 결합할 수 있음. -> query set을 단 한번만 정의하면됨
# Router 를 사용함으로써 URL 설정을 다룰 필요가 없음.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
