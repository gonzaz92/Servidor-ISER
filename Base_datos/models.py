from django.db import models
from django.core.validators import MaxValueValidator

def subida_documentacion(instace, filename):
    return f"documentación/{instace.display_name()}/{instace.apellido}_{instace.nombre}/{filename}"

class Locutor_nacional(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    formulario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    DNI = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    pdf_dni = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    secundario = models.CharField(max_length=100, null='True', blank=True)
    pdf_secundario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    instituto = models.CharField(max_length=100, null='True', blank=True)
    pdf_instituto = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    acta = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    habilitación = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_expediente = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_expediente = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_disposición = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_disposición = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)

    def display_name(self):
        return "Locutor-a Nacional"

class Locutor_local(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    formulario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    DNI = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    pdf_dni = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    secundario = models.CharField(max_length=100, null='True', blank=True)
    pdf_secundario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    localidad = models.CharField(max_length=100, null='True', blank=True)
    provincia = models.CharField(max_length=100, null='True', blank=True)
    certificado = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    acta = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    habilitación = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_expediente = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_expediente = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_disposición = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_disposición = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)

    def display_name(self):
        return "Locutor-a Local"

class Operador_nacional_radio(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    formulario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    DNI = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    pdf_dni = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    secundario = models.CharField(max_length=100, null='True', blank=True)
    pdf_secundario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    instituto = models.CharField(max_length=100, null='True', blank=True)
    pdf_instituto = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    acta = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    habilitación = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_expediente = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_expediente = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_disposición = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_disposición = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)

    def display_name(self):
        return "Operador-a de Radio"

class Operador_nacional_tv(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    formulario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    DNI = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    pdf_dni = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    secundario = models.CharField(max_length=100, null='True', blank=True)
    pdf_secundario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    instituto = models.CharField(max_length=100, null='True', blank=True)
    pdf_instituto = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    acta = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    habilitación = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_expediente = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_expediente = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_disposición = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_disposición = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)

    def display_name(self):
        return "Operador-a de TV"

class Operador_nacional_planta(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    formulario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    DNI = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    pdf_dni = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    secundario = models.CharField(max_length=100, null='True', blank=True)
    pdf_secundario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    instituto = models.CharField(max_length=100, null='True', blank=True)
    pdf_instituto = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    acta = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    habilitación = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_expediente = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_expediente = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_disposición = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_disposición = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)

    def display_name(self):
        return "Operador-a de Planta"

class Operador_local_radio(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    formulario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    DNI = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    pdf_dni = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    secundario = models.CharField(max_length=100, null='True', blank=True)
    pdf_secundario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    localidad = models.CharField(max_length=100, null='True', blank=True)
    provincia = models.CharField(max_length=100, null='True', blank=True)
    certificado = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    acta = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    habilitación = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_expediente = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_expediente = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_disposición = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_disposición = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)

    def display_name(self):
        return "Operador-a Local Radio"

class Operador_local_tv(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    formulario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    DNI = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    pdf_dni = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    secundario = models.CharField(max_length=100, null='True', blank=True)
    pdf_secundario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    localidad = models.CharField(max_length=100, null='True', blank=True)
    provincia = models.CharField(max_length=100, null='True', blank=True)
    certificado = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    acta = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    habilitación = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_expediente = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_expediente = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_disposición = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_disposición = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)

    def display_name(self):
        return "Operador-a Local TV"

class Operador_local_planta(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    formulario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    DNI = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    pdf_dni = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    secundario = models.CharField(max_length=100, null='True', blank=True)
    pdf_secundario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    localidad = models.CharField(max_length=100, null='True', blank=True)
    provincia = models.CharField(max_length=100, null='True', blank=True)
    certificado = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    acta = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    habilitación = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_expediente = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_expediente = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_disposición = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_disposición = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)

    def display_name(self):
        return "Operador-a Local Planta"

class Productor(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    formulario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    DNI = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    pdf_dni = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    secundario = models.CharField(max_length=100, null='True', blank=True)
    pdf_secundario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    instituto = models.CharField(max_length=100, null='True', blank=True)
    pdf_instituto = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    acta = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    habilitación = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_expediente = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_expediente = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_disposición = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_disposición = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)

    def display_name(self):
        return "Productor-a y Director-a"

class Guionista(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    formulario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    DNI = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    pdf_dni = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    secundario = models.CharField(max_length=100, null='True', blank=True)
    pdf_secundario = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    instituto = models.CharField(max_length=100, null='True', blank=True)
    pdf_instituto = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    acta = models.FileField(upload_to=subida_documentacion, null='True', blank=True)
    habilitación = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_expediente = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_expediente = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)
    año_disposición = models.IntegerField(validators=[MaxValueValidator(9999)], null='True', blank=True)
    número_disposición = models.IntegerField(validators=[MaxValueValidator(999999999)], null='True', blank=True)

    def display_name(self):
        return "Guionista"