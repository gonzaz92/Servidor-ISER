from django.db.models.signals import post_save
from django.dispatch import receiver
from Base_datos.models import (Locutor_nacional, Locutor_local,
                               Operador_nacional_radio, Operador_nacional_tv, Operador_nacional_planta,
                               Operador_local_radio, Operador_local_tv, Operador_local_planta)

def actualizar_items_relacionados(sender, instance, **kwargs):
    try:
        if getattr(instance, '_skip_signal', False):
            return
        
        items_relacionados = sender.objects.filter(año_expediente=instance.año_expediente, número_expediente=instance.número_expediente)
        for item in items_relacionados:
            item._skip_signal = True  # Establece el flag para evitar el loop
            item.año_expediente = instance.año_expediente
            item.número_expediente = instance.número_expediente
            item.año_disposición = instance.año_disposición
            item.número_disposición = instance.número_disposición
            item.save()
    except Exception as e:
        print(f"No Funciona: {e}, {sender}")

@receiver(post_save, sender=Locutor_nacional)
def post_save_locutor_nacional(sender, instance, **kwargs):
    actualizar_items_relacionados(sender, instance, **kwargs)

@receiver(post_save, sender=Locutor_local)
def post_save_locutor_local(sender, instance, **kwargs):
    actualizar_items_relacionados(sender, instance, **kwargs)

@receiver(post_save, sender=Operador_nacional_radio)
def post_save_operador_nacional_radio(sender, instance, **kwargs):
    actualizar_items_relacionados(sender, instance, **kwargs)

@receiver(post_save, sender=Operador_nacional_tv)
def post_save_operador_nacional_tv(sender, instance, **kwargs):
    actualizar_items_relacionados(sender, instance, **kwargs)

@receiver(post_save, sender=Operador_nacional_planta)
def post_save_operador_nacional_planta(sender, instance, **kwargs):
    actualizar_items_relacionados(sender, instance, **kwargs)

@receiver(post_save, sender=Operador_local_radio)
def post_save_operador_local_radio(sender, instance, **kwargs):
    actualizar_items_relacionados(sender, instance, **kwargs)

@receiver(post_save, sender=Operador_local_tv)
def post_save_operador_local_tv(sender, instance, **kwargs):
    actualizar_items_relacionados(sender, instance, **kwargs)

@receiver(post_save, sender=Operador_local_planta)
def post_save_operador_local_planta(sender, instance, **kwargs):
    actualizar_items_relacionados(sender, instance, **kwargs)
