from rest_framework import serializers
from google_books_app.models.author_models import AuthorModel
from google_books_app.validators.not_blank import not_blank

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = [
            'id',
            'name'
        ]
        extra_kwargs = {
            'name': {
                'required': True,
                'validators': [not_blank('name')]
            }
        }
        