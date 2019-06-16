from django.contrib import admin
from usuario.models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
	list_display = ['usuario', 'matricula', 'cargo']


# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)