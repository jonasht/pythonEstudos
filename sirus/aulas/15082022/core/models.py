from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(models.Model):
    # verbose_name_plural 
    verbose_name = "Usuario"
    
class BaseModel(models.Model):
    tipo_Movimentacao = (('entrada', 'Entrada'), ('saida', 'Saida'))
    valor = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    data = models.DateField(null=True)
    tipo = models.CharField(choices=tipo_Movimentacao)
    usuario = models.ForeignKey()

