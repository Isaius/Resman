from django.contrib import admin
from django.urls import path, include
from .views import reservar_recurso, listar_reservas

urlpatterns = [
	path('new/', reservar_recurso, name="nova_reserva"),
    path('new/<str:recurso_id>', reservar_recurso, name="nova_reserva_recurso"),
    path('listar/', listar_reservas, name="listar_reservas"),
]