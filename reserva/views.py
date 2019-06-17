from django.shortcuts import render
from django.http import HttpResponse
from .forms import ReservarForm, VisReservaForm
from .models import Reserva
from recurso.models import Recurso
from datetime import date

# Create your views here.
def visualizar_reserva(request, reserva_id):
	reserva = Reserva.objects.get(pk=reserva_id)
	form = VisReservaForm(initial={
			'identificador': reserva.identificador,
			'recurso': reserva.recurso,
			'usuario': reserva.usuario,
			'data_reserva': reserva.data_reserva,
			'tempo_alocacao': reserva.tempo_alocacao
		})
	return render(request, 'visualizar_reserva.html', {'form': form})

def listar_reservas(request):
	reservas = Reserva.objects.all()
	for r in reservas:
		print(r)
	return render(request, 'listar_reservas.html', {'reservas': reservas})

def reservar_recurso(request):
	form = ReservarForm(request.POST)

	if form.is_valid():
		idt = form.cleaned_data['identificador']
		rec = form.cleaned_data['recurso']
		usu = form.cleaned_data['usuario']
		data_r = form.cleaned_data['data_reserva']
		tempo_a = form.cleaned_data['tempo_alocacao']

		#if tempo_a > rec.TMA:
		#	print('Tempo máximo de alocacao excedido: ' + str(tempo_a) + ', '
		#		+ 'recurso' + rec.__str__() + ' tem tma ' + str(rec.TMA))
		#	return render(request, 'reserva_recurso.html', {'form': form})

		reserva = Reserva(
			identificador=idt,
			recurso=rec,
			usuario=usu,
			data_reserva=data_r,
			tempo_alocacao=tempo_a
		)

		try:
			reserva.save()
			print('Reserva ' + reserva.__str__() + ' salva com sucesso')
		except:
			print('Ocorreu um erro ao salvar a reserva')
		
	return render(request, 'reserva_recurso.html', {'form': form})