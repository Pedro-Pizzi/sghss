from django.db import models
from cryptography.fernet import Fernet
from django.conf import settings

fernet = Fernet(settings.ENCRYPTION_KEY)

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf_criptografado = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    historico_clinico = models.TextField(blank=True)

    @property
    def cpf(self):
        try:
            return fernet.decrypt(self.cpf_criptografado.encode()).decode()
        except:
            return None

    @cpf.setter
    def cpf(self, value):
        self.cpf_criptografado = fernet.encrypt(value.encode()).decode()

    def __str__(self):
        return self.nome

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=50)
    crm = models.CharField(max_length=20, unique=True)

class Consulta(models.Model):
    TIPO_CHOICES = [('presencial', 'Presencial'), ('online', 'Online')]
    data_hora = models.DateTimeField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)

class Leito(models.Model):
    numero = models.CharField(max_length=10)
    disponivel = models.BooleanField(default=True)

class Receita(models.Model):
    medicamentos = models.TextField()
    validade = models.DateField()
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE)