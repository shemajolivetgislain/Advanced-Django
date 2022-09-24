from django.contrib import admin
from django.urls import path, include
from watchlist_app.api.views import StreamPlatformDetail, WatchDetail, WatchListAV, streamPlatform
# from watchlist_app.api.views import movie_list,Get_movie

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:movie_id>', WatchDetail.as_view(), name='got-movie'),

    path('stream', streamPlatform.as_view(), name='stream-list'),
    path('stream/<int:stream_id>', StreamPlatformDetail.as_view(), name='stream-detail'),
]
