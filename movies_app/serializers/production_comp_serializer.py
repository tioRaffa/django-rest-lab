from rest_framework import serializers
from movies_app.validators.not_blank import not_blank
from movies_app.models import ProductionCompaniesModel

class ProductionCompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionCompaniesModel
        fields = [
            'id',
            'name',
            'origin_country',
            'logo_path',
            'tmdb_id'
        ]
        extra_kwargs = {
            'name': {
                'required': True,
                'validators': [not_blank('name')]
            },
            'origin_country': {
                'required': True,
                'validators': [not_blank('origin_country')]
            },
            'logo_path': {
                'required': True,
                'validators': [not_blank('logo_path')]
            },
            'tmdb_id': {
                'write_only': True,
                'required': True
            }
        }