from rest_framework import serializers
from .models import User # 선언한 모델

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # 선언한 모델을 model 값에 넣어주는 작업
        fields = ('id','username','age','city') # 필드 설정