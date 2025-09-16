from rest_framework import serializers

def not_blank(field_name):
    def validator(value):
        if isinstance(value, str) and len(value.strip()) == 0:
            raise serializers.ValidationError(
                f"O campo '{field_name}' não pode estar vazio!"
            )
        return value
    return validator

