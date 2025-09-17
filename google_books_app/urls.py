from django.urls import path
from google_books_app.views import SearchBookByTitle, ListCreateAPIView, RetriveUpdateAPIView


urlpatterns = [
    path('admin/search_book/', SearchBookByTitle.as_view(), name='Search_book'),
    path('books/', ListCreateAPIView.as_view(), name='ListCreate_book'),
    path('books/<int:pk>/', RetriveUpdateAPIView.as_view(), name='RetriveUpdate_book'),
]
