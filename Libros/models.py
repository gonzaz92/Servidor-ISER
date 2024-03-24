from django.db import models
from django.contrib.auth.models import User

notas = (
    ('AUSENTE', 'AUSENTE'),
    ('1 (Uno con 00/100)', '1 (Uno con 00/100)'),
    ('1,50 (Uno con 50/100)', '1,50 (Uno con 50/100)'),
    ('2 (Dos con 00/100)', '2 (Dos con 00/100)'),
    ('2,50 (Dos con 50/100)', '2,50 (Dos con 50/100)'),
    ('3 (Tres con 00/100)', '3 (Tres con 00/100)'),
    ('3,50 (Tres con 50/100)', '3,50 (Tres con 50/100)'),
    ('4 (Cuatro con 00/100)', '4 (Cuatro con 00/100)'),
    ('4,50 (Cuatro con 50/100)', '4,50 (Cuatro con 50/100)'),
    ('5 (Cinco con 00/100)', '5 (Cinco con 00/100)'),
    ('5,50 (Cinco con 50/100)', '5,50 (Cinco con 50/100)'),
    ('6 (Seis con 00/100)', '6 (Seis con 00/100)'),
    ('6,50 (Seis con 50/100)', '6,50 (Seis con 50/100)'),
    ('7 (Siete con 00/100)', '7 (Siete con 00/100)'),
    ('7,50 (Siete con 50/100)', '7,50 (Siete con 50/100)'),
    ('8 (Ocho con 00/100)', '8 (Ocho con 00/100)'),
    ('8,50 (Ocho con 50/100)', '8,50 (Ocho con 50/100)'),
    ('9 (Nueve con 00/100)', '9 (Nueve con 00/100)'),
    ('9,50 (Nueve con 50/100)', '9,50 (Nueve con 50/100)'),
    ('10 (Diez con 00/100)', '10 (Diez con 00/100)'),
)

cantidad = (
    ('0 (cero)', '0 (cero)'),
    ('1 (uno)', '1 (uno)'),
    ('2 (dos)', '2 (dos)'),
    ('3 (tres)', '3 (tres)'),
    ('4 (cuatro)', '4 (cuatro)'),
    ('5 (cinco)', '5 (cinco)'),
    ('6 (seis)', '6 (seis)'),
    ('7 (siete)', '7 (siete)'),
    ('8 (ocho)', '8 (ocho)'),
    ('9 (nueve)', '9 (nueve)'),
    ('10 (diez)', '10 (diez)'),
    ('11 (once)', '11 (once)'),
    ('12 (doce)', '12 (doce)'),
    ('13 (trece)', '13 (trece)'),
    ('14 (catorce)', '14 (catorce)'),
    ('15 (quince)', '15 (quince)'),
    ('16 (dieciséis)', '16 (dieciséis)'),
    ('17 (diecisiete)', '17 (diecisiete)'),
    ('18 (dieciocho)', '18 (dieciocho)'),
    ('19 (diecinueve)', '19 (diecinueve)'),
    ('20 (veinte)', '20 (veinte)'),
    ('21 (veintiuno)', '21 (veintiuno)'),
    ('22 (veintidós)', '22 (veintidós)'),
    ('23 (veintitrés)', '23 (veintitrés)'),
    ('24 (veinticuatro)', '24 (veinticuatro)'),
    ('25 (veinticinco)', '25 (veinticinco)'),
)

examenes = (
    ('Ingreso', 'Ingreso'),
    ('Habilitación', 'Habilitación'),
)

categorias = (
    ('Locutor/a Nacional', 'Locutor/a Nacional'),
    ('Operador/a Nacional de Radio', 'Operador/a Nacional de Radio'),
    ('Operador/a Nacional de TV', 'Operador/a Nacional de TV'),
    ('Operador/a Nacional de Planta Transmisora', 'Operador/a Nacionales de Planta Transmisora'),
    ('Productor/a y Director/a para Radio y TV', 'Productor/a y Director/a para Radio y TV'),
    ('Guionista de Radio y TV', 'Guionista de Radio y TV'),
)

class Firma(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='firma')
    imagen = models.ImageField(upload_to='firmas', null='True', blank=True)

    def __str__(self):
        return self.user.last_name + ',' + ' ' + self.user.first_name
    
    def ver_imagen(self):
        return self.imagen

class Libro(models.Model):
    nombre = models.CharField(max_length=200, unique=True, verbose_name='Nombre del instituto')

    def __str__(self):
        return f'{self.nombre.upper()}'

class Acta(models.Model):
    fecha = models.DateField()
    instituto = models.ForeignKey(Libro, on_delete=models.CASCADE, to_field='nombre', verbose_name='Instituto')
    examen = models.CharField(max_length=50, choices=examenes, verbose_name='Examen')
    carrera = models.CharField(max_length=100, choices=categorias,verbose_name='Carrera')
    profesores = models.CharField(max_length=200, verbose_name='Profesores')
    persona1 = models.CharField(max_length=100, verbose_name='Alumno 1')
    dni1 = models.CharField(max_length=10, verbose_name='D.N.I. alumno 1')
    nota1 = models.CharField(max_length=100, choices=notas, verbose_name='Nota alumno 1')
    persona2 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 2')
    dni2 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 2')
    nota2 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 2')
    persona3 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 3')
    dni3 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 3')
    nota3 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 3')
    persona4 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 4')
    dni4 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 4')
    nota4 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 4')
    persona5 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 5')
    dni5 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 5')
    nota5 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 5')
    persona6 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 6')
    dni6 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 6')
    nota6 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 6')
    persona7 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 7')
    dni7 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 7')
    nota7 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 7')
    persona8 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 8')
    dni8 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 8')
    nota8 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 8')
    persona9 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 9')
    dni9 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 9')
    nota9 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 9')
    persona10 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 10')
    dni10 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 10')
    nota10 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 10')
    persona11 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 11')
    dni11 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 11')
    nota11 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 11')
    persona12 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 12')
    dni12 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 12')
    nota12 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 12')
    persona13 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 13')
    dni13 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 13')
    nota13 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 13')
    persona14 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 14')
    dni14 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 14')
    nota14 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 14')
    persona15 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 15')
    dni15 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 15')
    nota15 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 15')
    persona16 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 16')
    dni16 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 16')
    nota16 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 16')
    persona17 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 17')
    dni17 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 17')
    nota17 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 17')
    persona18 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 18')
    dni18 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 18')
    nota18 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 18')
    persona19 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 19')
    dni19 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 19')
    nota19 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 19')
    persona20 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 20')
    dni20 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 20')
    nota20 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 20')
    persona21 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 21')
    dni21 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 21')
    nota21 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 21')
    persona22 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 22')
    dni22 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 22')
    nota22 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 22')
    persona23 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 23')
    dni23 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 23')
    nota23 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 23')
    persona24 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 24')
    dni24 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 24')
    nota24 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 24')
    persona25 = models.CharField(max_length=100, null='True', blank=True, verbose_name='Alumno 25')
    dni25 = models.CharField(max_length=10, null='True', blank=True, verbose_name='D.N.I. alumno 25')
    nota25 = models.CharField(max_length=100, choices=notas, null='True', blank=True, verbose_name='Nota alumno 25')
    total = models.CharField(max_length=100, choices=cantidad, verbose_name='Total')
    aprobados = models.CharField(max_length=100, choices=cantidad, verbose_name='Aprobados')
    desaprobados = models.CharField(max_length=100, choices=cantidad, verbose_name='Desaprobados')
    ausentes = models.CharField(max_length=100, choices=cantidad, verbose_name='Ausentes')
    firma1 = models.ForeignKey(Firma, on_delete=models.CASCADE, null='True', blank=True, related_name='acta_firma1')
    firma2 = models.ForeignKey(Firma, on_delete=models.CASCADE, null='True', blank=True, related_name='acta_firma2')
    firma3 = models.ForeignKey(Firma, on_delete=models.CASCADE, null='True', blank=True, related_name='acta_firma3')

