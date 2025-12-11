from django.db import models

# Create your models here.
from django.db import models

class Sala(models.Model):
    numero = models.CharField(max_length=10, unique=True)  # "301", "302", etc.

    def __str__(self):
        return f"Sala {self.numero}"


class HorarioSala(models.Model):
    DIAS_SEMANA = [
        (0, "Lunes"),
        (1, "Martes"),
        (2, "Miércoles"),
        (3, "Jueves"),
        (4, "Viernes"),
        (5, "Sábado"),
        (6, "Domingo"),
    ]

    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    dia_semana = models.IntegerField(choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()

    asignatura = models.CharField(max_length=100)
    docente = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.sala} - {self.asignatura} ({self.hora_inicio}-{self.hora_termino})"
