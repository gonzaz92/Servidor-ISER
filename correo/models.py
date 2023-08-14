from django.db import models

def subida_documentacion(instance, filename):
    return f"documentación/correo/{instance.destinatario}/{filename}"

class Correo(models.Model):
    envio = models.DateField(verbose_name='Fecha de Envío')
    destinatario = models.CharField(max_length=100, verbose_name='Destinatario')
    direccion = models.CharField(max_length=100, verbose_name='Dirección de Envío')
    seguimiento = models.CharField(max_length=15, verbose_name='Número de Seguimiento')
    acuse = models.FileField(upload_to=subida_documentacion, null='True', blank=True, verbose_name='Acuse de Recibo')
