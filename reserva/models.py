from django.db import models
from recurso.models import Recurso

# Create your models here.
class Reserva(models.Model):
	identificador = models.CharField('Identificador', max_length=10, primary_key=True)
	'''Membro'''
	recurso = models.ForeignKey(Recurso, on_delete=models.DO_NOTHING)
	data_solicitacao = models.DateTimeField('Solicitado em', auto_now_add=True)	# auto_now_add - acho que faz sentido ser assim
	data_reserva = models.DateTimeField('Reservado para')
	tempo_alocacao = models.PositiveIntegerField('Tempo de alocação') # limitado pelo tma do recurso reservado