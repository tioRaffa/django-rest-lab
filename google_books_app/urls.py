from django.urls import path
from google_books_app.views import SearchBookByTitle


urlpatterns = [
    path('admin/search_book/', SearchBookByTitle.as_view(), name='Search_book'),
]
