from django.contrib import admin
from reserva.models import Reserva


class ReservaAdmin(admin.ModelAdmin):
	list_display = ['identificador', 'recurso', 'usuario', 'data_solicitacao']


# Register your models here.
admin.site.register(Reserva, ReservaAdmin)