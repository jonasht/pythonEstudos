import email
from django.db import models

# Create your models here.

SEXO_CHOICES = (
    ('m', 'masculino'),
    ('f', 'feminino'),
    ('o', 'outro')
)

class Perfil(models.Model):
    nome = models.CharField(max_length=25, blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    sexo = models.CharField(max_length=1,
        choices=SEXO_CHOICES, blank=True, null=True)
    email = models.EmailField(max_length=30, blank=True, null=True)

    def __str__(self) -> str:
        return self.nome
