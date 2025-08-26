from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ContatosModel(Base):
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email', unique=True)
    phone = PhoneNumberField(region='BR', blank=True, null=True)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return f'Contato de - {self.name}'