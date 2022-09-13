# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse
# # Create your views here.
# # list all objects
# def movie_list(request):
#     movie = Movie.objects.all()
#     data = {
#         'movie' : list(movie.values()),
#     }
#     return JsonResponse(data)

# def Get_movie(request, movie_id):
#     get_movie = Movie.objects.get(id=movie_id)
#     data = {
#         'name' : get_movie.name,
#         'description' : get_movie.description,
#         'active': get_movie.active,
#     }
#     return JsonResponse(data)