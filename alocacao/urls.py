from django.contrib import admin
from django.urls import path, include
from .views import alocar_reserva, listar_alocacoes

urlpatterns = [
	path('nova/', alocar_reserva, name="alocar_reserva"),
	path('listar/', listar_alocacoes, name='listar_alocacoes')
]