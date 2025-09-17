from os import name
from django.forms import ValidationError
from rest_framework import serializers
from google_books_app.models.book_model import BookModel
from google_books_app.validators.not_blank import not_blank, validate_isbn, validate_page_count

from google_books_app.serializer.author_serializer import AuthorSerializer
from google_books_app.models.author_models import AuthorModel
from google_books_app.serializer.category_serializer import CategorySerializer
from google_books_app.models.category_model import CategoryModel


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    authors_ids = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset = AuthorModel.objects.all(),
        source='authors',
        many=True,
        required=False,
        help_text='Id de autores'
    )
    categories = CategorySerializer(many=True)
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
            'buy_link',
            'price',
            'currency',
            'slug'
        ]
        extra_kwargs = {
            'slug': {
                'write_only': True,
                'validators': [not_blank('slug')]
            },
            'google_book_id': {
                'write_only': True,
                'validators': [not_blank('google_book_id')]
            },
            'title': {'validators': [not_blank('title')]},
            'description': {'validators': [not_blank('description')]},
            'isbn_10': {'validators': [validate_isbn]},
            'isbn_13': {'validators': [validate_isbn]},
            'page_count': {'validators': [validate_page_count]},
        }
        
        
    def create(self, validated_data):
        authors_data = validated_data.pop('authors', [])
        categories_data = validated_data.pop('categories', [])
        
        book = BookModel.objects.create(**validated_data)
        
        try:
            book.full_clean()
        except ValueError as e:
            raise serializers.ValidationError(e)
        
        if authors_data:
            for author_data in authors_data:
                author, created = AuthorModel.objects.get_or_create(name=author_data.get('name'))
                book.authors.add(author)
                
        if categories_data:
            for category_data in categories_data:
                category, created = CategoryModel.objects.get_or_create(name=category_data.get('name'))
                book.categories.add(category)
        
        return book
    
    
    def update(self, instance, validated_data):
        authors_data = validated_data.pop('authors', None)
        categories_data = validated_data.pop('categories', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        try:
            instance.full_clean()
        except ValueError as e:
            raise serializers.ValidationError(e)
        
        if authors_data is not None:
            instance.authors.add(*authors_data)
        if categories_data is not None:
            instance.categories.add(*categories_data)
        
        instance.save()
        return instance