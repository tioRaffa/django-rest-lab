from django.db import models

# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Course(Base):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.title
    

class Avaliação(Base):
    curso = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='avaliacoes')
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    nota_avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = [
            'email',
            'curso'
        ]

    def __str__(self):
        return f'{self.nome} avaliou o curso - {self.curso} - {self.nota_avaliacao}'
    