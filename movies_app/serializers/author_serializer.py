from rest_framework import serializers
from movies_app.models.author_model import AuthorModel
from movies_app.validators.not_blank import not_blank

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = [
            'id',
            'name',
            'known_for_department',
            'profile_path',
            'tmdb_id'
        ]
        extra_kwargs = {
            'name': {
                'required': True,
                'validators': [not_blank('name')]
            },
            'kwnown_for_department':{
                'required': True,
                'validators': [not_blank('known_for_department')]
            },
            'profile_path': {
                'required': True,
                'validators': [not_blank('profile_path')]
            },
            'tmdb_id': {'write_only': True, 'required': True}
        }
        