from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from api.filters import DateFilter
from api.models import Movie, Comment
from api.serializers import MovieSerializer, CommentSerializer, TopSerializer, MovieInputSerializer

from api.utils import make_api_call


class MovieViewSet(ModelViewSet):
    """Movie (list/retrieve/delete/update) endpoint
    note: retrieve added on purpose - I see no reason
    to skip it with update made possible
    """

    serializer_class = MovieSerializer
    title_serializer_class = MovieInputSerializer
    queryset = Movie.objects.all()

    def create(self, request):
        serializer = self.title_serializer_class(data=request.data)
        if serializer.is_valid():
            title = serializer.data['title']
            try:
                obj = Movie.objects.get(title__iexact=title)
                movie = self.serializer_class(obj)
            except Movie.DoesNotExist:
                data = make_api_call(title)
                movie = self.serializer_class(data=data)
                if movie.is_valid():
                    movie.save()
            return Response(movie.data)
        return Response(status=400, data=serializer.errors)


class CommentAPIView(ListAPIView,
                     CreateAPIView):
    """Comment (POST/GET) endpoint
    GET:
    returns all comments on GET request,
    allows filtering with additional ?movie_id query
    parameter
    POST:
    allows to add a comment on movie, requires
    movie id and comment content eg:
    {"movie": 1, "content": "Some content"}
    """

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('movie_id',)


class TopAPIView(ListAPIView):
    """
    Returns top commented movies, allows to filter
    based on date range, required format is:
    ?created_at_min=2019-12-01&created_at_max=2020-01-30
    """
    serializer_class = TopSerializer
    filterset_class = DateFilter
    filter_backends = (filters.DjangoFilterBackend,)
    queryset = Movie.objects.order_by('-comments_count')
