from django.forms import ModelForm
from django import forms
from .models import Reserva
from recurso.models import Recurso

class ReservarForm(ModelForm):
	class Meta:
		model = Reserva
		fields = ['identificador', 'recurso', 'usuario', 'data_reserva', 'tempo_alocacao']

	def clean(self):
		cleaned_data = super().clean()
		print(cleaned_data.get('tempo_alocacao'))

		tma_reserva = cleaned_data.get('tempo_alocacao')
		recurso = cleaned_data.get('recurso')
		if recurso is not None:
			if tma_reserva > recurso.TMA:
				self.add_error('tempo_alocacao', 'Tempo de alocação não pode exceder ' + str(recurso.TMA) + ' horas.')

		return cleaned_data