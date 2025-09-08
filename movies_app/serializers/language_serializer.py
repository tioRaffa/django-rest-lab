from rest_framework import serializers
from movies_app.models import LanguagesModel
from movies_app.validators.not_blank import not_blank


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguagesModel
        fields = [
            'id',
            'language',
            'iso_639_1'
        ]
        extra_kwargs = {
            'language': {
                'required': True,
                'validators': [not_blank('language')]
            },
            'iso_639_1': {
                'required': True,
                'validators': [not_blank('iso_639_1')]
            }
        }