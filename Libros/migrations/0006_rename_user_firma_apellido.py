# Generated by Django 4.2.1 on 2024-05-23 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Libros', '0005_firma_nombre_alter_firma_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firma',
            old_name='user',
            new_name='apellido',
        ),
    ]