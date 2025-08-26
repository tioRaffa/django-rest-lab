from django.db import models

# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)

    class Meta:
        abstract = True


class TaskModel(Base):
    title = models.CharField('Titulo', max_length=100,)
    description = models.TextField('Descrição', blank=True, null=True)