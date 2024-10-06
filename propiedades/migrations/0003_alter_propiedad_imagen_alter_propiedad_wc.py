# Generated by Django 5.1.1 on 2024-10-02 07:47

import propiedades.context_processors
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades', '0002_alter_propiedad_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='imagen',
            field=models.ImageField(blank=True, upload_to=propiedades.context_processors.get_unique_filename, verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='wc',
            field=models.IntegerField(),
        ),
    ]