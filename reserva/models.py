from django.db import models
from recurso.models import Recurso
from usuario.models import Usuario

# Create your models here.
class Reserva(models.Model):
	identificador = models.CharField('Identificador', max_length=10, primary_key=True)
	recurso = models.ForeignKey(Recurso, on_delete=models.DO_NOTHING)
	usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
	data_solicitacao = models.DateTimeField('Solicitado em', auto_now_add=True)	# auto_now_add - acho que faz sentido ser assim
	data_reserva = models.DateTimeField('Data e hora para reserva')
	tempo_alocacao = models.PositiveIntegerField('Tempo de alocação') # limitado pelo tma do recurso reservado

	objects = models.Manager()

	class Meta:
		verbose_name = 'Reserva'
		verbose_name_plural = 'Reservas'
		ordering = ('data_solicitacao',)

	def __str__(self):
		return self.identificador