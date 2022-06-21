from django.contrib import admin
from django.urls import path, include

from watchlist_app.views import movie_list

urlpatterns = [
    path('movie/', movie_list, name='movie-list')
]
