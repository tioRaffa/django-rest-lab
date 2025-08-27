from django.contrib import admin
from book.models import CategoryModel, BooksModel
# Register your models here.

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'created_at',
        'updated_at',
        'is_active'
    ]
    ordering = ['-id']


@admin.register(BooksModel)
class BooksAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'description',
        'author',
        'category',
        'created_at',
        'is_active',
    ]
    ordering = ['-id']