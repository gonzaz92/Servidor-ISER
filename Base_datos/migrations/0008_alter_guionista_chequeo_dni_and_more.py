# Generated by Django 4.1.3 on 2024-05-09 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_datos', '0007_guionista_chequeo_expediente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guionista',
            name='chequeo_dni',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='guionista',
            name='chequeo_expediente',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='guionista',
            name='chequeo_formulario',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='guionista',
            name='chequeo_insti',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='guionista',
            name='chequeo_secu',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='locutor_local',
            name='chequeo_certi',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='locutor_local',
            name='chequeo_dni',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='locutor_local',
            name='chequeo_expediente',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='locutor_local',
            name='chequeo_formulario',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='locutor_local',
            name='chequeo_secu',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='locutor_nacional',
            name='chequeo_dni',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='locutor_nacional',
            name='chequeo_expediente',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='locutor_nacional',
            name='chequeo_formulario',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='locutor_nacional',
            name='chequeo_insti',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='locutor_nacional',
            name='chequeo_secu',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_local_planta',
            name='chequeo_certi',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_local_planta',
            name='chequeo_dni',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_local_planta',
            name='chequeo_expediente',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_local_planta',
            name='chequeo_formulario',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_local_planta',
            name='chequeo_secu',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_local_radio',
            name='chequeo_certi',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_local_radio',
            name='chequeo_dni',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_local_radio',
            name='chequeo_expediente',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_local_radio',
            name='chequeo_formulario',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_local_radio',
            name='chequeo_secu',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_local_tv',
            name='chequeo_certi',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_local_tv',
            name='chequeo_dni',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_local_tv',
            name='chequeo_expediente',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_local_tv',
            name='chequeo_formulario',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_local_tv',
            name='chequeo_secu',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_nacional_planta',
            name='chequeo_dni',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_nacional_planta',
            name='chequeo_expediente',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_nacional_planta',
            name='chequeo_formulario',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_nacional_planta',
            name='chequeo_insti',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_nacional_planta',
            name='chequeo_secu',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_nacional_radio',
            name='chequeo_dni',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_nacional_radio',
            name='chequeo_expediente',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_nacional_radio',
            name='chequeo_formulario',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_nacional_radio',
            name='chequeo_insti',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_nacional_radio',
            name='chequeo_secu',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_nacional_tv',
            name='chequeo_dni',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_nacional_tv',
            name='chequeo_expediente',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_nacional_tv',
            name='chequeo_formulario',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_nacional_tv',
            name='chequeo_insti',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='operador_nacional_tv',
            name='chequeo_secu',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='productor',
            name='chequeo_dni',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='productor',
            name='chequeo_expediente',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='productor',
            name='chequeo_formulario',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='productor',
            name='chequeo_insti',
            field=models.BooleanField(default=False, null='True'),
        ),
        migrations.AlterField(
            model_name='productor',
            name='chequeo_secu',
            field=models.BooleanField(default=False, null='True'),
        ),
    ]