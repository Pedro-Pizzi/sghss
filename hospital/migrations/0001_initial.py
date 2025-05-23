# Generated by Django 5.2.1 on 2025-05-20 02:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('disponivel', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('data_nascimento', models.DateField()),
                ('historico_clinico', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('especialidade', models.CharField(max_length=50)),
                ('crm', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField()),
                ('tipo', models.CharField(choices=[('presencial', 'Presencial'), ('online', 'Online')], max_length=10)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.paciente')),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.profissional')),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicamentos', models.TextField()),
                ('validade', models.DateField()),
                ('consulta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hospital.consulta')),
            ],
        ),
    ]
