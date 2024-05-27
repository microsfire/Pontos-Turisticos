from django.db import models
from apps.atracoes.models import Atracao
from apps.comentarios.models import Comentario
from apps.avaliacoes.models import Avaliacao
from apps.enderecos.models import Endereco


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False) 
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    campo_teste = models.CharField(max_length=100, null=True, blank=True)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
    