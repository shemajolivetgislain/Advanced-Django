from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
    # validating all object to be not the same
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and description should be different")
        else:
            return data
#    validating single field 
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Name is too short!")
        return value