# Generated by Django 5.0.3 on 2024-04-23 04:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacina', '0003_alter_vacina_vacina_fabricante_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarioVacina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dose', models.CharField(choices=[('1ª dose', '1ª dose'), ('2ª dose', '2ª dose'), ('3ª dose', '3ª dose'), ('4ª dose', '4ª dose'), ('6ª dose', '6ª dose'), ('dose unica', 'dose unica'), ('reforço', 'reforço')], max_length=20, verbose_name='Dose')),
                ('vacina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacina.vacina')),
            ],
        ),
    ]
