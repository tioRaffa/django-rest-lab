from .base import BaseModel
from django.db import models


class ProductionCompaniesModel(BaseModel):
    name = models.CharField('Nome Produtora', max_length=200)
    origin_country = models.CharField('Origem', max_length=3, blank=True, null=True)
    logo_path = models.CharField('LogoTipo', max_length=200)
    tmdb_id = models.IntegerField('ID pordutora')

    class Meta:
        verbose_name = 'Produtora'
        verbose_name_plural = 'Produtoras'

    def __str__(self):
        return self.name