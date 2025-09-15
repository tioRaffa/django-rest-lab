from tabnanny import verbose
from .base_model import BaseModel
from django.db import models


class AuthorModel(BaseModel):
    name = models.CharField(max_length=150, verbose_name='Nome', unique=True)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return self.name
    
    