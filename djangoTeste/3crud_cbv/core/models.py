from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nome

