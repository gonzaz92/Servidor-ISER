from django.db import models
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from datetime import date

tipos_de_estado = (
    ('Armado ISER', 'Armado ISER'),
    ('Revisión ISER', 'Revisión ISER'),
    ('Revisión DNSA', 'Revisión DNSA'),
    ('Esperando Dictamen', 'Esperando Dictamen'),
    ('Firma de Disposición', 'Firma de Disposición'),
    ('Hacer carnet', 'Hacer carnet'),
    ('Finalizado', 'Finalizado'),
)

categorias = (
    ('Locutores Nacionales', 'Locutores Nacionales'),
    ('Locutores Locales', 'Locutores Locales'),
    ('Operadores Nacionales Varios', 'Operadores Nacionales Varios'),
    ('Operadores Nacionales de Radio', 'Operadores Nacionales de Radio'),
    ('Operadores Nacionales de TV', 'Operadores Nacionales de TV'),
    ('Operadores Nacionales de Planta Transmisora', 'Operadores Nacionales de Planta Transmisora'),
    ('Operadores Locales Varios', 'Operadores Locales Varios'),
    ('Operadores Locales de Radio', 'Operadores Locales de Radio'),
    ('Operadores Locales de TV', 'Operadores Locales de TV'),
    ('Operadores Locales de Planta Transmisora', 'Operadores Locales de Planta Transmisora'),
    ('Productores y Directores para Radio y TV', 'Productores y Directores para Radio y TV'),
    ('Guionistas de Radio y TV', 'Guionistas de Radio y TV'),
)

def validar_numero(self):
    if not self.isnumeric():
        raise ValidationError('Solo ingrese números en el siguiente campo')

class Expediente(models.Model):
    Año_de_Expediente = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(9999)])
    Número_de_Expediente = models.CharField(max_length=9, null=True, blank=True, validators=[validar_numero])
    Fecha_de_Creación = models.DateField(null=True, blank=True, verbose_name='Fecha de Caratulación')
    Cantidad_de_Habilitados = models.IntegerField(null=True, blank=True)
    Instituto_o_Localidad = models.CharField(max_length=100)
    Categoría = models.CharField(max_length=43, choices=categorias)
    Fecha_de_disposición = models.DateField(null=True, blank=True)
    Estado = models.CharField(max_length=20, choices=tipos_de_estado)
    observaciones = models.TextField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha_asignado = models.DateField()
    aprobados = models.IntegerField(default=1)
    fecha_pase = models.DateField(null=True, blank=True)
    pase_legal = models.DateField(null=True, blank=True)