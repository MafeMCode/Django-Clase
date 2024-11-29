# Generated by Django 5.1.3 on 2024-11-29 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=60, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='Email')),
                ('dni', models.CharField(max_length=9, unique=True, verbose_name='Dni')),
                ('bio', models.TextField(blank=True, verbose_name='Biografía')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('cuerpo', models.TextField()),
                ('fpublicacion', models.DateField(default='2024-07-22')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.autor')),
            ],
        ),
    ]
