from rest_framework import serializers
from contatos.models import ContatosModel


class ContatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContatosModel
        fields = [
            'id',
            'name',
            'email',
            'phone',
            'created_at'
        ]
        extra_kwargs = {
            'email': {'write_only': True},
            'created_at': {'read_only': True}
        }