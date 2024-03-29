# Generated by Django 4.1.3 on 2023-10-18 01:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('correo', '0002_correo_categoria_correo_dni_correo_localidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='correo',
            name='carnet',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(999999999)], verbose_name='Carnet N°'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='correo',
            name='observaciones',
            field=models.TextField(blank=True, max_length=200, null='True', verbose_name='Observaciones'),
        ),
    ]
