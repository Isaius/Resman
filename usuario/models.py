from django.db import models
from recurso.models import Recurso

MEMBRO = 'membro'
RESP = 'responsavel'
ADMIN = 'administrador'
CARGO_CHOICES = [
	(MEMBRO, 'Membro'),
	(RESP, 'Responsável'),
	(ADMIN, 'Administrador'),
]


# Create your models here.
class Usuario(models.Model):
	matricula = models.CharField('Matrícula', max_length=10, primary_key=True)
	nome = models.CharField('Nome', max_length=140)
	usuario = models.CharField('Usuário', max_length=15, unique=True)
	setor = models.CharField('Setor', max_length=20)
	cargo = models.CharField('Cargo', max_length=13, choices=CARGO_CHOICES)
	recursos = models.ManyToManyField(Recurso)

	objects = models.Manager()

	class Meta:
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'
		ordering = ('usuario',)

	def __str__(self):
		return self.usuario