from django.db import models
import datetime

# Create your models here.
class BaseModel(models.Model):
    created_at: datetime.datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime.datetime = models.DateTimeField(auto_now=True)
    is_active: bool = models.BooleanField(default=True)

    objects: models.Manager = models.Manager()

    class Meta:
        abstract = True


class CategoryModel(BaseModel):
    name: str = models.CharField(max_length=100)

    class Meta:
        verbose_name= 'Categoria'
        verbose_name_plural= 'Categorias'

    def __str__(self) -> str:
        return self.name


class BooksModel(BaseModel):
    title: str = models.CharField('titulo', max_length=150)
    description: str = models.TextField('Descrição')
    author: str = models.CharField('Autor', max_length=100)
    category: CategoryModel = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='books')

    class Meta:
        verbose_name= 'Livro'
        verbose_name_plural= 'Livros'

    def __str__(self) -> str:
        return self.title

