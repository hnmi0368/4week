from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Movie


class MovieViewSet(viewsets.ModelViewSet):
    """
    영화 API
    ---
    영화에 대한 정보
    """

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

