from django.db import models
from reserva.models import Reserva

ATIV = 'ativa'
ENC = 'encerrada'
ESTADOS_CHOICES = [
	(ATIV, 'Ativa'),
	(ENC, 'Encerrada'),
]

# Create your models here.
class Alocacao(models.Model):
	identificador = models.CharField('Identificador', max_length=10, primary_key=True)
	reserva = models.ForeignKey(Reserva, on_delete=models.DO_NOTHING)
	estado = models.CharField('Estado', max_length=9, choices=ESTADOS_CHOICES)
	data_aprovacao = models.DateTimeField('Aprovado em', auto_now_add=True)
	data_entrega = models.DateTimeField('Devolvido em', null=True, blank=True)

	class Meta:
		verbose_name = 'Alocação'
		verbose_name_plural = 'Alocações'
		ordering = ('data_aprovacao',)

	def __str__(self):
		return self.identificador