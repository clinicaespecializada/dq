# Generated by Django 5.1 on 2024-08-27 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=155)),
                ('genero', models.CharField(max_length=155)),
                ('idade', models.IntegerField()),
                ('data_nascimento', models.DateField()),
                ('nacionalidade', models.CharField(max_length=155)),
                ('cidade_origem', models.CharField(max_length=155)),
                ('estado_civil', models.CharField(max_length=155)),
                ('escolaridade', models.CharField(max_length=155)),
                ('religiao', models.CharField(max_length=155)),
                ('situacao_profissional', models.CharField(max_length=155)),
                ('profissao', models.CharField(max_length=155)),
                ('filhos', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('1', 'ATIVO'), ('2', 'INATIVO'), ('3', 'TRIAGEM')], max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='EnderecoPaciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=155)),
                ('pais', models.CharField(max_length=155)),
                ('estado', models.CharField(max_length=155)),
                ('cidade', models.CharField(max_length=155)),
                ('bairro', models.CharField(max_length=155)),
                ('rua', models.CharField(max_length=155)),
                ('numero', models.IntegerField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=155)),
                ('telefone', models.CharField(max_length=155)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente')),
            ],
        ),
    ]