from django.forms import ModelForm
from django import forms
from .models import Reserva
from recurso.models import Recurso
from datetime import datetime, timedelta
from pytz import utc

class ReservarForm(ModelForm):
	class Meta:
		model = Reserva
		fields = ['identificador', 'recurso', 'usuario', 'data_reserva', 'tempo_alocacao']

	def clean(self):
		cleaned_data = super().clean()
		print(cleaned_data.get('tempo_alocacao'))

		# Validacao da data de reserva (nao pode ser menor antes do horario atual)
		data_r = cleaned_data.get('data_reserva')
		recurso = cleaned_data.get('recurso')
		if data_r is not None and recurso is not None:
			tmr = datetime.now() + timedelta(hours=recurso.TMR)
			tmr = utc.localize(tmr)
			if data_r < tmr:
				msg = 'Reservas apenas a partir de ' + tmr.strftime('%d/%m/%y, %H:%M') + '.'
				self.add_error('data_reserva', msg)

		# Validacao do tempo maximo de alocacao
		tma_reserva = cleaned_data.get('tempo_alocacao')
		if recurso is not None:
			if tma_reserva > recurso.TMA:
				msg = 'Tempo de alocação não pode exceder ' + str(recurso.TMA) + ' horas.'
				self.add_error('tempo_alocacao', msg)

		return cleaned_data