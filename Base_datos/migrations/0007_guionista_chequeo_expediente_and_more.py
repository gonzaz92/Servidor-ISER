# Generated by Django 4.1.3 on 2024-05-09 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_datos', '0006_guionista_chequeo_dni_guionista_chequeo_insti_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='guionista',
            name='chequeo_expediente',
            field=models.BooleanField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='locutor_local',
            name='chequeo_expediente',
            field=models.BooleanField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='locutor_nacional',
            name='chequeo_expediente',
            field=models.BooleanField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='operador_local_planta',
            name='chequeo_expediente',
            field=models.BooleanField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='operador_local_radio',
            name='chequeo_expediente',
            field=models.BooleanField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='operador_local_tv',
            name='chequeo_expediente',
            field=models.BooleanField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='operador_nacional_planta',
            name='chequeo_expediente',
            field=models.BooleanField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='operador_nacional_radio',
            name='chequeo_expediente',
            field=models.BooleanField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='operador_nacional_tv',
            name='chequeo_expediente',
            field=models.BooleanField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='productor',
            name='chequeo_expediente',
            field=models.BooleanField(null='True'),
            preserve_default='True',
        ),
    ]