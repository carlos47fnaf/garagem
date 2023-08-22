from django.db import models
from garagem.models import Cor, Categoria, Marca, Acessorio

class Veiculo(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Veiculos"