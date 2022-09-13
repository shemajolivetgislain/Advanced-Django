from watchlist_app.api.serializers import MovieSerializer
from watchlist_app.models import Movie
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies)
    return Response(serializer.data)

@api_view()
def  Get_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)