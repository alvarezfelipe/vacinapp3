# Generated by Django 5.0.3 on 2024-04-06 00:01

import django.db.models.deletion
import localflavor.br.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crianca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crianca_nome', models.CharField(max_length=250, verbose_name='Nome da criança')),
                ('crianca_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('crianca_rg', models.CharField(blank=True, max_length=250, verbose_name='RG da criança')),
                ('crianca_cpf', localflavor.br.models.BRCPFField(blank=True, max_length=14, verbose_name='CPF')),
                ('crianca_responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.pais')),
            ],
            options={
                'db_table': 'crianca',
                'ordering': ('crianca_nome',),
            },
        ),
    ]
