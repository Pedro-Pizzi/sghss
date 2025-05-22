from rest_framework import serializers
from .models import Paciente, Consulta, Leito, Receita, Profissional
from django.utils import timezone

class PacienteSerializer(serializers.ModelSerializer):
    cpf = serializers.CharField(write_only=True)  # só entra via POST, não aparece na resposta

    class Meta:
        model = Paciente
        fields = ['id', 'nome', 'cpf', 'data_nascimento', 'historico_clinico']

    def validate_cpf(self, value):
        cleaned = ''.join(filter(str.isdigit, value))
        if len(cleaned) != 11:
            raise serializers.ValidationError("CPF deve conter 11 dígitos numéricos.")
        return cleaned

    def create(self, validated_data):
        cpf = validated_data.pop('cpf')  # retira o CPF do dicionário
        paciente = Paciente(**validated_data)
        paciente.cpf = cpf  # usa o setter para criptografar
        paciente.save()
        return paciente

    def update(self, instance, validated_data):
        cpf = validated_data.pop('cpf', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if cpf:
            instance.cpf = cpf  # criptografa o novo CPF se fornecido
        instance.save()
        return instance

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

    def validate_data_hora(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError("A data da consulta deve ser no futuro.")
        return value

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'

class LeitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leito
        fields = '__all__'

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'
