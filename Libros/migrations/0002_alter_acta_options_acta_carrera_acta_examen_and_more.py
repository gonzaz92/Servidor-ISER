# Generated by Django 4.1.3 on 2024-03-25 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acta',
            options={'verbose_name': 'Acta', 'verbose_name_plural': 'Actas'},
        ),
        migrations.AddField(
            model_name='acta',
            name='carrera',
            field=models.CharField(choices=[('Locutor/a Nacional', 'Locutor/a Nacional'), ('Operador/a Nacional de Radio', 'Operador/a Nacional de Radio'), ('Operador/a Nacional de TV', 'Operador/a Nacional de TV'), ('Operador/a Nacional de Planta Transmisora', 'Operador/a Nacionales de Planta Transmisora'), ('Productor/a y Director/a para Radio y TV', 'Productor/a y Director/a para Radio y TV'), ('Guionista de Radio y TV', 'Guionista de Radio y TV')], default=0, max_length=100, verbose_name='Carrera'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acta',
            name='examen',
            field=models.CharField(choices=[('Ingreso', 'Ingreso'), ('Habilitación', 'Habilitación')], default=0, max_length=50, verbose_name='Examen'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni1',
            field=models.CharField(max_length=10, verbose_name='D.N.I. alumno 1'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni10',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 10'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni11',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 11'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni12',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 12'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni13',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 13'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni14',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 14'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni15',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 15'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni16',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 16'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni17',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 17'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni18',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 18'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni19',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 19'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni2',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 2'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni20',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 20'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni21',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 21'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni22',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 22'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni23',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 23'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni24',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 24'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni25',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 25'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni3',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 3'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni4',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 4'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni5',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 5'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni6',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 6'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni7',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 7'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni8',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 8'),
        ),
        migrations.AlterField(
            model_name='acta',
            name='dni9',
            field=models.CharField(blank=True, max_length=10, null='True', verbose_name='D.N.I. alumno 9'),
        ),
    ]
