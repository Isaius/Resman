from django.shortcuts import render
from django.http import HttpResponse
from reserva.models import Reserva
from .models import Alocacao
from .forms import AlocarForm

# Create your views here.
def listar_alocacoes(request):
	alocacoes = Alocacao.objects.all()
	for a in alocacoes:
		print(a)
	return render(request, 'listar_alocacoes.html', {'alocacoes': alocacoes})

def alocar_reserva(request):
	form = AlocarForm(request.POST)

	if form.is_valid():
		idt = form.cleaned_data['identificador']
		res = form.cleaned_data['reserva']
		est = form.cleaned_data['estado']
		d_ent = form.cleaned_data['data_entrega']

		alocacao = Alocacao(
			identificador=idt,
			reserva=res,
			estado=est,
			data_entrega=d_ent
		)

		try:
			alocacao.save()
			print('Alocacao ' + alocacao.__str__() + ' salva com sucesso')
		except:
			print('Ocorreu um erro ao salvar a reserva')

	return render(request, 'alocar_reserva.html', {'form': form})