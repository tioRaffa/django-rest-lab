from .base import BaseModel
from django.db import models

class DirectorModel(BaseModel):
    name = models.CharField('Nome', max_length=200)
    profile_path = models.CharField('Path do Perfil', max_length=250)
    tbmdb_id = models.IntegerField(unique=True)

    class Meta:
        verbose_name = 'Diretor'
        verbose_name_plural = 'Diretores'

    def __str__(self):
        return self.name