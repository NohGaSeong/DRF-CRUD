from rest_framework import serializers
from .models import User # 선언한 모델

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','age','city')