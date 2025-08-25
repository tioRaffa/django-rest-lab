from rest_framework import serializers
from .models import Course, Avaliação

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliação
        fields = [
            'curso',
            'nome',
            'email',
            'comentario',
            'nota_avaliacao',
            'created_at'
        ]
        extra_kwargs = {
            'email': {
                'write_only': True
            },
            'create_at': {
                'read_only': True
            }
        }



class CourseSerializer(serializers.ModelSerializer):
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'url',
            'avaliacoes',
            'created_at'
        ]
        extra_kwargs = {
            'id': {'read_only': True}
        }