from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer
from watchlist_app.models import WatchList, StreamPlatform
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class streamPlatform(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetail(APIView):

    def get(self, request, stream_id):
        try:
            platforms = StreamPlatform.objects.get(id=stream_id)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Stream platform not found'}, status=status.HTTP_404_NOT_FOUND )
        serializer = StreamPlatformSerializer(platforms)
        return Response(serializer.data)

    def put(self, request, stream_id):
        platform = StreamPlatform.objects.get(id=stream_id)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, stream_id):
        movie = StreamPlatform.objects.get(id=stream_id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetail(APIView):

    def get(self, request, movie_id):
        try:
            movie = WatchList.objects.get(id=movie_id)
        except WatchList.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND )
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, movie_id):
        movie = WatchList.objects.get(id=movie_id)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, movie_id):
        movie = WatchList.objects.get(id=movie_id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
   
# way 1 of doing ApI Views By using Function based views
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many = True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def  Get_movie(request, movie_id):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(id=movie_id)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND )
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         movie = Movie.objects.get(id=movie_id)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     if request.method == 'DELETE':
#         movie = Movie.objects.get(id=movie_id)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT) 
