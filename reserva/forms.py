from django.forms import ModelForm
from django import forms
from .models import Reserva
from .widgets import BootstrapDateTimePickerInput

class ReservarForm(ModelForm):
	class Meta:
		model = Reserva
		fields = ['identificador', 'recurso', 'usuario', 'data_reserva', 'tempo_alocacao']
