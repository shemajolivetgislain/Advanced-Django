from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    WatchList = WatchListSerializer(read_only = True, many = True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"

# class WatchListSerializer(serializers.ModelSerializer):
#     length_name = serializers.SerializerMethodField()
#     class Meta:
#         model = WatchList
#         fields = "__all__"
        # exclude = ['id']
# adding custom fields in serializer using this following function
#     def get_length_name(self, object):
#         return  len(object.name)
#     # validating all object to be not the same
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and description should be different")
#         else:
#             return data
# #    validating single field 
#     def validate_name(self, value):
#         if len(value) < 3:
#             raise serializers.ValidationError("Name is too short!")
#         return value