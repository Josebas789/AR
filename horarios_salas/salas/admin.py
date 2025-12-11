from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Sala, HorarioSala

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('numero',)

@admin.register(HorarioSala)
class HorarioSalaAdmin(admin.ModelAdmin):
    list_display = ('sala', 'dia_semana', 'hora_inicio', 'hora_termino', 'asignatura', 'docente')
    list_filter = ('dia_semana', 'sala')

