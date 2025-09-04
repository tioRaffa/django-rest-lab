from .base import BaseModel
from django.db import models
from .movie_model import MoviesModels


class VideoModel(BaseModel):
    name = models.CharField('Titulo Filme', max_length=200, blank=True, null=True)
    key = models.CharField('Chave', max_length=200)
    video_id = models.CharField('iD', max_length=200)
    site = models.CharField('Site', max_length=100, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)

    filme = models.ForeignKey(MoviesModels, on_delete=models.CASCADE, related_name='videos')

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.name or self.key