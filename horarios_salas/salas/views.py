from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.utils import timezone
from .models import Sala, HorarioSala

def horario_actual_sala(request, numero_sala):
    # numero_sala llega como "304", "301", etc.
    try:
        sala = Sala.objects.get(numero=numero_sala)
    except Sala.DoesNotExist:
        return JsonResponse({"error": "Sala no encontrada"}, status=404)

    ahora = timezone.localtime()
    dia = ahora.weekday()      # 0 = lunes, 6 = domingo
    hora = ahora.time()

    # Buscamos si hay un horario que cubra este momento
    horario = HorarioSala.objects.filter(
        sala=sala,
        dia_semana=dia,
        hora_inicio__lte=hora,
        hora_termino__gte=hora
    ).first()

    if horario is None:
        return JsonResponse({
            "sala": sala.numero,
            "asignatura": None,
            "docente": None,
            "inicio": None,
            "termino": None,
        })

    return JsonResponse({
        "sala": sala.numero,
        "asignatura": horario.asignatura,
        "docente": horario.docente,
        "inicio": horario.hora_inicio.strftime("%H:%M"),
        "termino": horario.hora_termino.strftime("%H:%M"),
    })
