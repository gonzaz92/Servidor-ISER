from django.contrib import admin
from .models import Libro, Acta,Firma

class LibroAdmin(admin.ModelAdmin):
    search_fields = ('nombre'),
    ordering = ['nombre']

class ActaAdmin(admin.ModelAdmin):
    ordering = ['fecha']
    autocomplete_fields = ['instituto']

admin.site.register(Libro, LibroAdmin)
admin.site.register(Acta, ActaAdmin)
admin.site.register(Firma)