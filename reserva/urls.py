from django.contrib import admin
from django.urls import path, include
from .views import reservar_recurso

urlpatterns = [
	path('new/', reservar_recurso, name="nova_reserva"),
    path('new/<str:recurso_id>', reservar_recurso, name="nova_reserva_recurso"),
]