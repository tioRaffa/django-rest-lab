from django.urls import path
from google_books_app.views import SearchBookByTitle
from google_books_app.views import ListCreateAPIView


urlpatterns = [
    path('admin/search_book/', SearchBookByTitle.as_view(), name='Search_book'),
    path('admin/books/', ListCreateAPIView.as_view(), name='ListCreate_book')
]
