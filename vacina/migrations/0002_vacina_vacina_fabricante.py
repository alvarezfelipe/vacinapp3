# Generated by Django 5.0.3 on 2024-04-04 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacina', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacina',
            name='vacina_fabricante',
            field=models.CharField(default=1, max_length=250, verbose_name='Lote'),
            preserve_default=False,
        ),
    ]
