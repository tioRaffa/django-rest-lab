from .base import BaseModel
from django.db import models


class AuthorModel(BaseModel):
    name = models.CharField('Nome', max_length=100)
    known_for_department = models.CharField('Area de Atuação', max_length=100)
    profile_path = models.CharField('Path foto de perfil', max_length=250)
    tmdb_id = models.IntegerField('Id author', unique=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.name