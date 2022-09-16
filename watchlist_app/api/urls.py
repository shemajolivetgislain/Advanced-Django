from django.contrib import admin
from django.urls import path, include
from watchlist_app.api.views import MovieList, MovieDetail
# from watchlist_app.api.views import movie_list,Get_movie

urlpatterns = [
    path('list/', MovieList.as_view(), name='movie-list'),
    path('<int:movie_id>',MovieDetail.as_view(), name='got-movie'),
]
