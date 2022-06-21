from django.shortcuts import render
from watchlist_app.models import Movie

# Create your views here.
def movie_list(request):
    movie = Movie.objects.all()
    print(movie)