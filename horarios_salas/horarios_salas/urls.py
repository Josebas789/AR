from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from salas.views import horario_actual_sala

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Página principal (sirve tu index.html)
    path('', TemplateView.as_view(template_name='index.html'), name='home'),

    # ✅ Tu API (igual que antes)
    path('api/sala/<str:numero_sala>/', horario_actual_sala, name='horario_actual_sala'),
]
