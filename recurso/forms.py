from django.forms import ModelForm
from django import forms
from .models import PesquisaRecursos

class Pesquisa_rec_form(ModelForm):
    class Meta:
        model = PesquisaRecursos
        fields = ['identificador', 'descricao', 'tipo', 'categoria', 'estado', 'setor']
      