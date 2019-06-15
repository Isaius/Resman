from django.db import models

DISP = 'disponivel'
RESERV = 'reservado'
INDISP = 'indisponivel'
EMP = 'emprestado'
ESTADOS_CHOICES = [
    (DISP, 'Disponível'),
    (RESERV, 'Reservado'),
    (INDISP, 'Indisponível'),
    (EMP, 'Emprestado'),
]

ESP = 'espaco'
ACC = 'acessorio'
PC = 'computador'
PROJ = 'projetor'
MOV = 'moveis'
CATEGORIA_CHOICES = [
    (ESP, 'Espaço'),
    (ACC, 'Acessórios'),
    (PC, 'Computadores'),
    (PROJ, 'Projetores'),
    (MOV, 'Móveis'),
]

POR = 'portatil'
NPOR = 'nportatil'
TIPO_CHOICES = [
    (POR, 'Portátil'),
    (NPOR, 'Não Portátil'),
]
# Create your models here.
class Recurso(models.Model):
    identificador = models.CharField(max_length=10, primary_key=True)
    descricao = models.CharField(max_length=140)
    tipo = models.CharField(max_length=15, choices = TIPO_CHOICES)
    categoria = models.CharField(max_length=20, choices = CATEGORIA_CHOICES)
    estado = models.CharField(max_length=20, choices = ESTADOS_CHOICES, default = DISP,)
    setor = models.CharField(max_length=20)
    TMA = models.IntegerField()
    TMR = models.IntegerField()
    TMAP = models.IntegerField()
    MDI = models.CharField(max_length=140, blank=True)

    objects = models.Manager()
    def __str__(self):
        return self.descricao

class PesquisaRecursos(models.Model):
    identificador = models.CharField(max_length=10, blank=True)
    descricao = models.CharField(max_length=140, blank=True)
    tipo = models.CharField(max_length=15, choices = TIPO_CHOICES, blank=True)
    categoria = models.CharField(max_length=20, choices = CATEGORIA_CHOICES, blank=True)
    estado = models.CharField(max_length=20, choices = ESTADOS_CHOICES, default = DISP, blank=True)
    setor = models.CharField(max_length=20, blank=True)

    objects = models.Manager()
    def __str__(self):
        return self.descricao