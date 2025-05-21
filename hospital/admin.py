from django.contrib import admin
from .models import Paciente, Consulta, Profissional, Leito, Receita

admin.site.register(Paciente)
admin.site.register(Consulta)
admin.site.register(Profissional)
admin.site.register(Leito)
admin.site.register(Receita)