from tabnanny import verbose
from .base_model import BaseModel
from django.db import models


class CategoryModel(BaseModel):
    name = models.CharField(max_length=150, unique=True, verbose_name='Nome')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.name