from rest_framework import serializers
from google_books_app.validators.not_blank import not_blank
from google_books_app.models.category_model import CategoryModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = [
            'id',
            'name'
        ]
        extra_kwargs = {
            'name': {
                'required': True,
                'validators': [not_blank('Name')]
            }
        }