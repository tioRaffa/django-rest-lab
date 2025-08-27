from django.urls import path
from book.views import BooksAPIView, BookAPIView

urlpatterns = [
    path('books/', BooksAPIView.as_view(), name='Livros'),
    path('book/<int:pk>/', BookAPIView.as_view(), name='Livro')
]