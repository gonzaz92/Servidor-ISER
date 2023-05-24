from django.db import models
from django.core.validators import MaxValueValidator

tipos_de_estado = (
    ('Revisión ISER', 'Revisión ISER'),
    ('Revisión DNSA', 'Revisión DNSA'),
    ('Esperando Dictamen', 'Esperando Dictamen'),
    ('Firma de Disposición', 'Firma de Disposición'),
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

class Expediente(models.Model):
    Año_de_Expediente = models.IntegerField(validators=[MaxValueValidator(9999)])
    Número_de_Expediente = models.IntegerField(validators=[MaxValueValidator(999999999)])
    Fecha_de_Creación = models.DateField()
    Cantidad_de_Habilitados = models.IntegerField()
    Instituto_o_Localidad= models.CharField(max_length=100)
    Categoría = models.CharField(max_length=43, choices=categorias)
    Fecha_de_disposición = models.DateField(null='True', blank=True)
    Estado = models.CharField(max_length=20, choices=tipos_de_estado)

    def formatted_fecha_creacion(self, fecha):
        return fecha.strftime('%d-%m-%Y')

    def save(self, *args, **kwargs):
        # Convertir la fecha de creación a una cadena de texto antes de guardarla
        self.Fecha_de_Creación = str(self.Fecha_de_Creación)
        super().save(*args, **kwargs)