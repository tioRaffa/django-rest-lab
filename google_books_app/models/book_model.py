from .base_model import BaseModel
from django.db import models

class BookModel(BaseModel):
    google_book_id = models.CharField(max_length=22, verbose_name='Google ID', unique=True)
    title = models.CharField(max_length=250, verbose_name='Titulo')
    publisher = models.CharField(max_length=100, verbose_name='Editora')
    published_date = models.CharField(max_length=50, verbose_name='Data de Publicação')
    description = models.TextField(verbose_name='Descrição')
    page_count = models.PositiveIntegerField(verbose_name='Numero de Paginas')
    
    author = ... #many to many
    categories = ... # many to many
    
    thumbnail_url = models.URLField(verbose_name='URL da capa')
    
    isbn_10 = models.CharField(max_length=10, unique=True, verbose_name='ISBN 10', blank=True, null=True)
    isbn_13 = models.CharField(max_length=13, unique=True, verbose_name='ISBN 13')
    
    
    class Meta:
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['isbn_13']),
            models.Index(fields=['google_book_id'])
        ]
        
    def __str__(self):
        return self.title