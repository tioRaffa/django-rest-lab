from django.contrib import admin

from google_books_app.models.author_models import AuthorModel
from google_books_app.models.book_model import BookModel
from google_books_app.models.category_model import CategoryModel


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'published_date', 'page_count')
    search_fields = ('title', 'publisher', 'isbn_10', 'isbn_13')
    list_filter = ('publisher', 'authors', 'categories')
    filter_horizontal = ('authors', 'categories')


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)