from rest_framework import serializers
from book.models import CategoryModel, BooksModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = [
            'id',
            'name',
            'created_at'
        ]


class BooksSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=CategoryModel.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = BooksModel
        fields = [
            'id',
            'title',
            'description',
            'author',
            'category',
            'category_id',
            'created_at',
            'is_active',
        ]