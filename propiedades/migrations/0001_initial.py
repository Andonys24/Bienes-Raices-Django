# Generated by Django 5.1.1 on 2024-10-02 06:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imagen', models.ImageField(blank=True, upload_to='propiedades')),
                ('descripcion', models.TextField()),
                ('habitaciones', models.IntegerField()),
                ('wc', models.DecimalField(decimal_places=1, max_digits=2)),
                ('estacionamientos', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualiacion', models.DateTimeField(auto_now=True)),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendedores.vendedor')),
            ],
        ),
    ]
