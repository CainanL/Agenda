from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nome  # retorna para o django o nome da categoria, assim fica mais facil visualizar no painél adminstrativo

# Create your models here.


class Contato(models.Model):  # contato está escrito no singular porque ele adiciona um "s" ao final
    # definições de colunas
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d')  # cria uma pasta foto com uma pasta ano dentro, com uma pasta mês dentro, com uma pasta dia dentro.

    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome
