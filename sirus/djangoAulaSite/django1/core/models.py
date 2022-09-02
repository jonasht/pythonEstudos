from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=15)
    estoque = models.IntegerField('qtd no estoque')
    imagem = models.ImageField('IMG', blank=True, upload_to='core')
    usuario = models.ForeignKey(
        User, null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='usuario_produto',
        
        )

    
    def __str__(self) -> str:
        return self.nome
        
class Cliente(models.Model):
    nome = models.CharField('nome', max_length=100)
    sobrenome = models.CharField('sobrenome', max_length=100)
    email = models.EmailField('email', max_length=150, unique=True)
    data_nascimento = models.DateField('data nascimento', blank=True, null=True)

