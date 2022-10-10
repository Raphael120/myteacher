from django.forms import ValidationError
from rest_framework import serializers

from .models import Aula, Professor


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class CadastrarAulaSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=255)

    def validate_nome(self, value):
        if len(value) < 3:
            raise ValidationError("Deve ter pelo menos 3 caracteres")
        return value


class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'
