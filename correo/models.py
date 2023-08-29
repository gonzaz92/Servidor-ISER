from django.db import models

def subida_documentacion(instance, filename):
    return f"documentación/correo/{instance.destinatario.upper()}_{instance.nombre.capitalize()}/{filename}"

class Correo(models.Model):
    envio = models.DateField(verbose_name='Fecha de Envío')
    destinatario = models.CharField(max_length=100, verbose_name='Apellido')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    direccion = models.CharField(max_length=100, verbose_name='Dirección de Envío')
    seguimiento = models.CharField(max_length=15, verbose_name='Número de Seguimiento')
    acuse = models.FileField(upload_to=subida_documentacion, null='True', blank=True, verbose_name='Acuse de Recibo')
