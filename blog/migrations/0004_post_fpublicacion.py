# Generated by Django 5.1.3 on 2024-11-27 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_delete_alumno'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fpublicacion',
            field=models.DateField(default='2024-07-22'),
        ),
    ]
