from django.db import models
from django.core.validators import MaxValueValidator

class Persona(models.Model):
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    año_formulario = models.IntegerField(validators=[MaxValueValidator(9999)], null=True, blank=True, verbose_name='Año Formulario')
    formulario = models.IntegerField(validators=[MaxValueValidator(999999999)], null=True, blank=True, verbose_name='Número GDE - Formulario')
    chequeo_formulario = models.BooleanField(null=True, default=False)
    DNI = models.IntegerField(validators=[MaxValueValidator(999999999)], null=True, blank=True, verbose_name='Documento N°')
    año_dni = models.IntegerField(validators=[MaxValueValidator(9999)], null=True, blank=True, verbose_name='Año DNI')
    pdf_dni = models.IntegerField(validators=[MaxValueValidator(999999999)], null=True, blank=True, verbose_name='Número GDE - D.N.I.')
    chequeo_dni = models.BooleanField(null=True, default=False)
    secundario = models.IntegerField(validators=[MaxValueValidator(9999)], null=True, blank=True, verbose_name='Año Secundario')
    pdf_secundario = models.IntegerField(validators=[MaxValueValidator(999999999)], null=True, blank=True, verbose_name='Número GDE - Secundario')
    chequeo_secu = models.BooleanField(null=True, default=False)
    año_acta = models.IntegerField(validators=[MaxValueValidator(9999)], null=True, blank=True, verbose_name='Año Acta')
    acta = models.IntegerField(validators=[MaxValueValidator(999999999)], null=True, blank=True, verbose_name='Número GDE - Acta de Examen')
    habilitación = models.IntegerField(validators=[MaxValueValidator(999999999)], null=True, blank=True, verbose_name='Número de Habilitación')
    año_expediente = models.IntegerField(validators=[MaxValueValidator(9999)], null=True, blank=True, verbose_name='Año Expediente')
    número_expediente = models.IntegerField(validators=[MaxValueValidator(999999999)], null=True, blank=True, verbose_name='Número GDE - Expediente')
    chequeo_expediente = models.BooleanField(null=True, default=False)
    año_disposición = models.IntegerField(validators=[MaxValueValidator(9999)], null=True, blank=True, verbose_name='Año Disposición')
    número_disposición = models.IntegerField(validators=[MaxValueValidator(999999999)], null=True, blank=True, verbose_name='Número GDE - Disposición')
    año_acuse = models.IntegerField(validators=[MaxValueValidator(9999)], null=True, blank=True, verbose_name='Año Acuse de Recibo')
    acuse = models.IntegerField(validators=[MaxValueValidator(999999999)], null=True, blank=True, verbose_name='Número GDE - Acuse de Recibo')
    caja = models.CharField(max_length=100, null=True, blank=True, verbose_name='Caja')
    observaciones = models.TextField(null=True, blank=True)
    
    class Meta:
        abstract = True
        permissions = [('view_complete_and_incomplete', 'view complete and incomplete')]
    
    def __str__(self):
        return f'{self.apellido.upper()}, {self.nombre.capitalize()}, {self.DNI}'

class Nacional(models.Model):
    instituto = models.CharField(max_length=100, null=True, blank=True, verbose_name='Egresado de')
    año_instituto = models.IntegerField(validators=[MaxValueValidator(9999)], null=True, blank=True, verbose_name='Año Analítico del Instituto')
    pdf_instituto = models.IntegerField(validators=[MaxValueValidator(999999999)], null=True, blank=True, verbose_name='Número GDE - Analítico del Instituto')
    chequeo_insti = models.BooleanField(null=True, default=False)

    class Meta:
        abstract = True

class Local(models.Model):
    localidad = models.CharField(max_length=100, null=True, blank=True, verbose_name='Localidad')
    provincia = models.CharField(max_length=100, null=True, blank=True, verbose_name='Provincia')
    año_certificado = models.IntegerField(validators=[MaxValueValidator(9999)], null=True, blank=True, verbose_name='Año Certificado Laboral')
    certificado = models.IntegerField(validators=[MaxValueValidator(999999999)], null=True, blank=True, verbose_name='Número GDE - Certificado Laboral')
    chequeo_certi = models.BooleanField(null=True, default=False)
    inicio_tad = models.DateField(null=True, blank=True)
    reclamo_tad = models.DateField(null=True, blank=True)


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
        return "Operador-a Nacional de Radio"

class Operador_nacional_tv(Persona, Nacional):
    def display_name(self):
        return "Operador-a Nacional de TV"

class Operador_nacional_planta(Persona, Nacional):
    def display_name(self):
        return "Operador-a Nacional de Planta"

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