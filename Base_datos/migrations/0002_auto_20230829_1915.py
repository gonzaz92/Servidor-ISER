# Generated by Django 3.2.18 on 2023-08-29 22:15

import Base_datos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_datos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guionista',
            name='acuse',
            field=models.FileField(blank=True, null='True', upload_to=Base_datos.models.subida_documentacion),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='locutor_local',
            name='acuse',
            field=models.FileField(blank=True, null='True', upload_to=Base_datos.models.subida_documentacion),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='locutor_nacional',
            name='acuse',
            field=models.FileField(blank=True, null='True', upload_to=Base_datos.models.subida_documentacion),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='operador_local_planta',
            name='acuse',
            field=models.FileField(blank=True, null='True', upload_to=Base_datos.models.subida_documentacion),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='operador_local_radio',
            name='acuse',
            field=models.FileField(blank=True, null='True', upload_to=Base_datos.models.subida_documentacion),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='operador_local_tv',
            name='acuse',
            field=models.FileField(blank=True, null='True', upload_to=Base_datos.models.subida_documentacion),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='operador_nacional_planta',
            name='acuse',
            field=models.FileField(blank=True, null='True', upload_to=Base_datos.models.subida_documentacion),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='operador_nacional_radio',
            name='acuse',
            field=models.FileField(blank=True, null='True', upload_to=Base_datos.models.subida_documentacion),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='operador_nacional_tv',
            name='acuse',
            field=models.FileField(blank=True, null='True', upload_to=Base_datos.models.subida_documentacion),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='productor',
            name='acuse',
            field=models.FileField(blank=True, null='True', upload_to=Base_datos.models.subida_documentacion),
            preserve_default='True',
        ),
    ]