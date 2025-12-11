from django.contrib import admin
from django.urls import path
from salas.views import horario_actual_sala

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sala/<str:numero_sala>/', horario_actual_sala, name='horario_actual_sala'),
]
