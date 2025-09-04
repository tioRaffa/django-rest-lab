from django.db import models

# Create your models here.

class MoviesModels(models.Model):
    title = models.CharField('Titulo', max_length=150)
    # Diretor
    overview = models.TextField('Sinopse')
    #genero
    release_date = models.DateField('Data de Lançamento')
    original_language = models.CharField('Idioma Original', max_length=3)
    runtime = models.IntegerField('Duração em Minutos')
    indicative_rating = models.CharField('Classificação Indicativa', max_length=100)
    
    vote_average = models.FloatField('Média de Votos')
    vote_count = models.IntegerField('Total de Votos')
    
    image = models.URLField('URL da Imagem')
    video = models.URLField('URL do Trailer')
    status = models.CharField('Status', max_length=40)
    
    budget = models.IntegerField('Orçamento') # Orçamento
    revenue = models.IntegerField('Receita')  # Receita
    popularity = models.FloatField('Popularidade')

    # idoma disponivel

    # Elenco
    #production_companies
    imdb_id = models.CharField('Id imdb', max_length=50)