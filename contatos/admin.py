from django.contrib import admin
from contatos.models import ContatosModel
# Register your models here.

@admin.register(ContatosModel)
class ContatoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'phone',
        'created_at'
    ]
    ordering = ['-id']