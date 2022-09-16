# from wsgiref.validate import validator
# from xml.dom import ValidationErr
# from rest_framework import serializers
# from watchlist_app.models import Movie

# # funtion for validating field
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
# # validating all object to be not the same
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and description should be different")
#         else:
#             return data
# #    validating single field 
#     # def validate_name(self, value):
#     #     if len(value) < 3:
#     #         raise serializers.ValidationError("Name is too short!")
#     #     return value
        


# # class MoviesSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Movie
# #         fields = ['id', 'name', 'description', 'active']

# # types of Validation

# # 1. field level validation
# # 2. object level validation
# # 3. function level validation by using validators