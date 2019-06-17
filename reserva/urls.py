from django.contrib import admin
from django.urls import path, include
from .views import reservar_recurso, listar_reservas, visualizar_reserva

urlpatterns = [
	path('new/', reservar_recurso, name="nova_reserva"),
    path('new/<str:recurso_id>', reservar_recurso, name="nova_reserva_recurso"),
    path('listar/', listar_reservas, name="listar_reservas"),
    path('visualizar/<str:reserva_id>', visualizar_reserva, name="visualizar_reserva"),
]