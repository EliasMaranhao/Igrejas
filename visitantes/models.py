from django.db import models
from datetime import datetime

# Create your models here.

class Visitante(models.Model):

    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True)
    data_visita = models.DateTimeField(default=datetime.now())
    evangelico = models.BooleanField(default=False)
    primeira_vez = models.BooleanField(default=True)
    igreja_origem = models.CharField(max_length=200, default='Não pertence a nenhuma igreja')
    pastor = models.CharField(max_length=200, blank=True)
    observacao = models.TextField(max_length=1000, blank=True)
    como_conheceu_igreja = models.CharField(max_length=200)