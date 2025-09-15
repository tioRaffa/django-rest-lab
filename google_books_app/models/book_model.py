from tabnanny import verbose
from .base_model import BaseModel
from django.db import models

from .author_models import AuthorModel
from .category_model import CategoryModel

class BookModel(BaseModel):
    google_book_id = models.CharField(max_length=22, verbose_name='Google ID', unique=True)
    title = models.CharField(max_length=250, verbose_name='Titulo')
    publisher = models.CharField(max_length=100, verbose_name='Editora', blank=True, null=True)
    published_date = models.CharField(max_length=50, verbose_name='Data de Publicação', blank=True, null=True)
    description = models.TextField(verbose_name='Descrição', blank=True, null=True)
    page_count = models.PositiveIntegerField(verbose_name='Numero de Paginas', blank=True, null=True)
    
    authors = models.ManyToManyField(AuthorModel, related_name='books', verbose_name='Autores', blank=True)
    categories = models.ManyToManyField(CategoryModel, related_name='books', verbose_name='Categorias', blank=True)
    
    thumbnail_url = models.URLField(verbose_name='URL da capa', blank=True, null=True)
    
    isbn_10 = models.CharField(max_length=10, unique=True, verbose_name='ISBN 10', blank=True, null=True)
    isbn_13 = models.CharField(max_length=13, unique=True, verbose_name='ISBN 13',blank=True, null=True)
    
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['isbn_13']),
            models.Index(fields=['google_book_id'])
        ]

        
    def __str__(self):
        return self.title