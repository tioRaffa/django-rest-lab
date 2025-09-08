from rest_framework import serializers
from movies_app.models import Gender
from movies_app.validators.not_blank import not_blank


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = [
            'id',
            'name',
            'tmdb_id'
        ]
        extra_kwargs = {
            'name': {
                'required': True,
                'validators': [not_blank('name')]
            },
            'tmdb_id': {
                'write_only': True,
                'required': True
            }
        }  
