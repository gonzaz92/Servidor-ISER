from django.db import models
from django.core.validators import MaxValueValidator

def subida_documentacion(instance, filename):
    return f"documentación/{instance.display_name()}/{instance.apellido.upper()}_{instance.nombre.capitalize()}/{filename}"

class Persona(models.Model):
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    formulario = models.FileField(upload_to=subida_documentacion, null='True', blank=True, verbose_name='Formulario')
    DNI = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True, verbose_name='Documento N°')
    pdf_dni = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    secundario = models.CharField(max_length=100, null='True', blank=True, verbose_name='Secundario')
    pdf_secundario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    acta = models.FileField(upload_to=subida_documentacion, null='True', blank=True, verbose_name='Acta de Examen')
    habilitación = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True, verbose_name='Número de Habilitación')
    año_expediente = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True, verbose_name='Año del Expediente')
    número_expediente = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True, verbose_name='Número del Expediente')
    año_disposición = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True, verbose_name='Año de la Disposición')
    número_disposición = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True, verbose_name='Número de la Disposición')
    acuse = models.FileField(upload_to=subida_documentacion, null='True', blank=True, verbose_name='Acuse')
    
    class Meta:
        abstract = True
        permissions = [('view_complete_and_incomplete', 'view complete and incomplete')]
    
    def __str__(self):
        return f'{self.apellido.upper()}, {self.nombre.capitalize()}, {self.DNI}'

class Nacional(models.Model):
    instituto = models.CharField(max_length=100, null='True', blank=True, verbose_name='Egresado de')
    pdf_instituto = models.FileField(upload_to=subida_documentacion, null='True', blank=True)

    class Meta:
        abstract = True

class Local(models.Model):
    localidad = models.CharField(max_length=100, null='True', blank=True, verbose_name='Localidad')
    provincia = models.CharField(max_length=100, null='True', blank=True, verbose_name='Provincia')
    certificado = models.FileField(upload_to=subida_documentacion, null='True', blank=True, verbose_name='Certificado Laboral')

    class Meta:
        abstract = True

class Locutor_nacional(Persona, Nacional):
    def display_name(self):
        return "Locutor-a Nacional"

class Locutor_local(Persona, Local):
    def display_name(self):
        return "Locutor-a Local"

class Operador_nacional_radio(Persona, Nacional):
    def display_name(self):
        return "Operador-a de Radio"

class Operador_nacional_tv(Persona, Nacional):
    def display_name(self):
        return "Operador-a de TV"

class Operador_nacional_planta(Persona, Nacional):
    def display_name(self):
        return "Operador-a de Planta"

class Operador_local_radio(Persona, Local):
    def display_name(self):
        return "Operador-a Local Radio"

class Operador_local_tv(Persona, Local):
    def display_name(self):
        return "Operador-a Local TV"

class Operador_local_planta(Persona, Local):
    def display_name(self):
        return "Operador-a Local Planta"

class Productor(Persona, Nacional):
    def display_name(self):
        return "Productor-a y Director-a"

class Guionista(Persona, Nacional):
    def display_name(self):
        return "Guionista"