from rest_framework import serializers
import re

def not_blank(field_name):
    def validator(value):
        if isinstance(value, str) and len(value.strip()) == 0:
            raise serializers.ValidationError(
                f"O campo '{field_name}' não pode estar vazio!"
            )
        return value
    return validator


def validate_isbn(value):
    if value:
        if not re.match(r'^\d{10}$|^\d{13}$', value):
            raise serializers.ValidationError("ISBN deve ter 10 ou 13 dígitos")
    return value


def validate_page_count(value):
    if value is not None and value <= 0:
        raise serializers.ValidationError("Número de páginas deve ser maior que zero")
    return value