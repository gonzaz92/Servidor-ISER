# Generated by Django 4.2.4 on 2024-11-05 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_datos', '0009_locutor_local_inicio_tad_locutor_local_reclamo_tad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='guionista',
            name='observaciones',
            field=models.TextField(blank=True, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='locutor_local',
            name='observaciones',
            field=models.TextField(blank=True, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='locutor_nacional',
            name='observaciones',
            field=models.TextField(blank=True, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='operador_local_planta',
            name='observaciones',
            field=models.TextField(blank=True, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='operador_local_radio',
            name='observaciones',
            field=models.TextField(blank=True, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='operador_local_tv',
            name='observaciones',
            field=models.TextField(blank=True, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='operador_nacional_planta',
            name='observaciones',
            field=models.TextField(blank=True, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='operador_nacional_radio',
            name='observaciones',
            field=models.TextField(blank=True, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='operador_nacional_tv',
            name='observaciones',
            field=models.TextField(blank=True, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='productor',
            name='observaciones',
            field=models.TextField(blank=True, null='True'),
            preserve_default='True',
        ),
    ]