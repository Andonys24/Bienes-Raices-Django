# Generated by Django 5.1.1 on 2024-10-02 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendedor',
            options={'ordering': ['-fecha_creacion'], 'verbose_name': 'Vendedor', 'verbose_name_plural': 'Vendedores'},
        ),
        migrations.RenameField(
            model_name='vendedor',
            old_name='fecha_actualiacion',
            new_name='fecha_actualizacion',
        ),
    ]
