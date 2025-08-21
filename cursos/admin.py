from django.contrib import admin
from .models import Course, Avaliação
# Register your models here.

@admin.register(Course)
class CursoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'url',
        'created_at',
        'is_active'
    ]

@admin.register(Avaliação)
class AvaliaçãoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
        'email',
        'comentario',
        'nota_avaliacao',
        'created_at',
        'is_active'
    ]