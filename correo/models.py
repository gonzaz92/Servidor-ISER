from django.db import models
from django.core.validators import MaxValueValidator
from expedientes.models import categorias, validar_numero

opciones = (
    ('Si', 'Si'),
    ('No', 'No'),
)

class Correo(models.Model):
    envio = models.DateField(verbose_name='Fecha de Envío')
    destinatario = models.CharField(max_length=100, verbose_name='Apellido')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    dni = models.IntegerField(validators=[MaxValueValidator(999999999)], verbose_name='D.N.I.')
    carnet = models.IntegerField(validators=[MaxValueValidator(999999999)], verbose_name='Carnet N°')
    direccion = models.CharField(max_length=100, verbose_name='Dirección de Envío')
    localidad = models.CharField(max_length=100, null='True', blank=True, verbose_name='Localidad')
    provincia = models.CharField(max_length=100, null='True', blank=True, verbose_name='Provincia')
    seguimiento = models.CharField(max_length=30, verbose_name='Número de Seguimiento')
    categoria = models.CharField(max_length=43, choices=categorias, verbose_name='Categoría')
    telefono = models.CharField(max_length=10, null='True', blank=True, verbose_name='Teléfono')
    mail = models.CharField(max_length=50, null='True', blank=True, verbose_name='e-mail')
    observaciones = models.TextField(max_length=200, null='True', blank=True, verbose_name='Observaciones')
    año_acuse = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True, verbose_name='Año')
    acuse = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True, verbose_name='Número')
    finalizado = models.CharField(max_length=43, choices=opciones, verbose_name='Finalizado')
