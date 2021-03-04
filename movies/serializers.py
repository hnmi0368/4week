from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Movie  # 모델 설정
        fields = ('id','title','genre','exp','dir','act','year','image') # 필드 설정
