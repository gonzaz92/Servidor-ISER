from django.db import models

class Correo(models.Model):
    envio = models.DateField(verbose_name='Fecha de Envío')
    destinatario = models.CharField(max_length=100, verbose_name='Destinatario')
    direccion = models.CharField(max_length=100, verbose_name='Dirección de Envío')
    seguimiento = models.CharField(max_length=15, verbose_name='Número de Seguimiento')
    acuse = models.FileField(null='True', blank=True, verbose_name='Acuse de Recibo')
