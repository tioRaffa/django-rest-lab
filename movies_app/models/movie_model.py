from django.db import models
from .base import BaseModel
from .director_model import DirectorModel
from .language_model import LanguagesModel
from .author_model import AuthorModel
from .production_companies_model import ProductionCompaniesModel
# Create your models here.

class Gender(BaseModel):
    name = models.CharField('Genero', max_length=100)
    tmdb_id = models.CharField('TMDB Id', max_length=50)
    
    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

    def __str__(self):
        return self.name


class MoviesModels(BaseModel):
    title = models.CharField('Titulo', max_length=150)
    directors = models.ManyToManyField(DirectorModel, related_name='filmes_dirigidos', blank=True, null=True)
    overview = models.TextField('Sinopse')
    genres = models.ManyToManyField(Gender, related_name='filmes', blank=True, null=True)
    release_date = models.DateField('Data de Lançamento')
    original_language = models.CharField('Idioma Original', max_length=3)
    runtime = models.IntegerField('Duração em Minutos')
    indicative_rating = models.CharField('Classificação Indicativa', max_length=100)
    vote_average = models.FloatField('Média de Votos')
    vote_count = models.IntegerField('Total de Votos')
    poster_path = models.CharField('Path do Poster', max_length=200)
    status = models.CharField('Status', max_length=40)
    budget = models.IntegerField('Orçamento') # Orçamento
    revenue = models.IntegerField('Receita')  # Receita
    popularity = models.FloatField('Popularidade')
    spoken_languages = models.ManyToManyField(LanguagesModel, related_name='filmes', blank=True, null=True)
    cast = models.ManyToManyField(AuthorModel, related_name='filmes_atuados', blank=True, null=True)
    production_companies = models.ManyToManyField(ProductionCompaniesModel, related_name='filmes_produzidos', blank=True, null=True)
    imdb_id = models.CharField('Id imdb', max_length=50, unique=True)
    # video

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'

    def __str__(self):
        return self.title