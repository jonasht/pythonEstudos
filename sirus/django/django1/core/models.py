from pyexpat import model
from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=15)
    estoque = models.IntegerField('qtd no estoque')
    
    def __str__(self) -> str:
        return self.nome
        
class Cliente(models.Model):
    nome = models.CharField('nome', max_length=100)
    sobrenome = models.CharField('sobrenome', max_length=100)
    email = models.EmailField('email', max_length=150, unique=True)
    data_nascimento = models.DateField('data nascimento', blank=True, null=True)

