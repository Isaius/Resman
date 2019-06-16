from django.shortcuts import render
from django.http import HttpResponse
from .forms import ReservarForm

# Create your views here.
def reservar_recurso(request):
	if request.method == 'POST':
		form = ReservarForm(request.POST)
		if form.is_valid():
			identificador = form.cleaned_data['identificador']
			return render(request, 'reserva_recurso.html', {'form': form})

	return render(request, 'reserva_recurso.html')