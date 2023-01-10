from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class Usuario(models.Model):
    nome = models.CharField(max_length=20)
    email = models.EmailField(max_length=20, unique=True, blank=False)
    cpf = models.CharField(max_length=20)
    rg = models.CharField(max_length=20)
    senha = models.CharField(max_length=20, blank=False)
    
    def __str__(self) -> str:
        return self.nome
        
    