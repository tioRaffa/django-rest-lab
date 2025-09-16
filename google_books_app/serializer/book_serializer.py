from rest_framework import serializers
from google_books_app.models.book_model import BookModel
from google_books_app.validators.not_blank import not_blank, validate_isbn, validate_page_count

from google_books_app.serializer.author_serializer import AuthorSerializer
from google_books_app.models.author_models import AuthorModel
from google_books_app.serializer.category_serializer import CategorySerializer
from google_books_app.models.category_model import CategoryModel


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(read_only=True, many=True)
    authors_ids = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset = AuthorModel.objects.all(),
        source='authors',
        many=True,
        required=False,
        help_text='Id de autores'
    )
    categories = CategorySerializer(read_only=True, many=True)
    categories_ids = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=CategoryModel.objects.all(),
        many=True,
        required=False,
        help_text='ID de categorias'
    )
    
    class Meta:
        model = BookModel
        fields = [
            'id',
            'google_book_id',
            'title',
            'publisher',
            'published_date',
            'description',
            'page_count',
            'authors',
            'authors_ids',
            'categories',
            'categories_ids',
            'thumbnail_url',
            'isbn_10',
            'isbn_13',
            'slug'
        ]
        extra_kwargs = {
            'slug': {
                'write_only': True,
                'validators': [not_blank('slug')]
            },
            'title': {'validators': [not_blank('title')]},
            'description': {'validators': [not_blank('description')]},
            'isbn_10': {'validators': [validate_isbn]},
            'isbn_13': {'validators': [validate_isbn]},
            'page_count': {'validators': [validate_page_count]},
        }
        
        
    # def create
    # def update
        
    