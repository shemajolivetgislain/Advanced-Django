from django.contrib import admin
from django.urls import path, include
from watchlist_app.api.views import WatchDetail, WatchList, streamPlatform
# from watchlist_app.api.views import movie_list,Get_movie

urlpatterns = [
    path('list/', WatchList.as_view(), name='movie-list'),
    path('<int:movie_id>', WatchDetail.as_view(), name='got-movie'),

    path('stream', streamPlatform.as_view(), name='stream-list'),
]
