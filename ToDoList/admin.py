from django.contrib import admin
from ToDoList.models import TaskModel
# Register your models here.

@admin.register(TaskModel)
class TaskADmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'description',
        'done',
        'created_at',
        'updated_at'
    ]
    ordering = ['-id']