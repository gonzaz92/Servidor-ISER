from django.apps import AppConfig


class BaseDatosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Base_datos'

    def ready(self):
        import Base_datos.signals