from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

 

# class MoviesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ['id', 'name', 'description', 'active']