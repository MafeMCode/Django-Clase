# Generated by Django 5.1.3 on 2024-11-27 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=60)),
                ('cuerpo', models.TextField()),
                ('fpublicacion', models.DateField(default='2024-07-22')),
            ],
        ),
    ]
