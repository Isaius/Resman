from django.contrib import admin
from .models import Alocacao


class AlocacaoAdmin(admin.ModelAdmin):
	list_display = ['identificador', 'reserva', 'estado', 'data_aprovacao']


# Register your models here.
admin.site.register(Alocacao, AlocacaoAdmin)