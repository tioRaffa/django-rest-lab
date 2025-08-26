from rest_framework import serializers
from ToDoList.models import TaskModel


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = [
            'id',
            'title',
            'description',
            'done',
            'created_at',
            'updated_at'
        ]
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True}
        }

