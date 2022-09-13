from django.contrib import admin
from django.urls import path, include

from watchlist_app.views import movie_list,Get_movie

urlpatterns = [
    path('movie/', movie_list, name='movie-list'),
    path('<int:movie_id>',Get_movie, name='got-movie'),
]
