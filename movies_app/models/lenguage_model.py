from .base import BaseModel
from django.db import models


class LanguagesModel(BaseModel):
    lenguage = models.CharField('Linguagem', max_length=100, unique=True)
    iso_639_1 = models.CharField('Abreviação', max_length=3)

    class Meta:
        verbose_name = 'Linguagem'
        verbose_name_plural = 'Linguagens'

    def __str__(self):
        return self.lenguage