from rest_framework import serializers
from movies_app.models.director_model import DirectorModel
from movies_app.validators.not_blank import not_blank

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectorModel
        fields = [
            'id',
            'name',
            'profile_path',
            'tmdb_id'
        ]
        extra_kwargs = {
            'name': {
                'required': True,
                'validators': [not_blank('name')]
            },
            'profile_path': {
                'required': True,
                'validators': [not_blank['profile_path']]
            },
            'tmdb_id': {'write_only': True, 'required': True}
        }