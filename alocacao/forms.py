from django.forms import ModelForm
from django import forms
from .models import Alocacao
from datetime import datetime, timedelta
from pytz import utc


class AlocarForm(ModelForm):
	class Meta:
		model = Alocacao
		fields = ['identificador', 'reserva', 'estado', 'data_entrega']

	def clean(self):
		cleaned_data = super().clean()

		#Validacao data de entrega
		d_entrega = cleaned_data.get('data_entrega')
		reserva = cleaned_data.get('reserva')
		if d_entrega is not None and reserva is not None:
			t_min_entrega = reserva.data_reserva + timedelta(hours=reserva.tempo_alocacao)
			t_min_entrega = utc.localize(t_min_entrega)
			if d_entrega < t_min_entrega:
				msg = 'Data de entrega, inválida o recurso está alocado até ' + t_min_entrega.strftime('%d/%m/%y, %H:%M') + '.'
				self.add_error('data_entrega', msg)

		return cleaned_data