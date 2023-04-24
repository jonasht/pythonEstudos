from unicodedata import category
from django.db import models
from django.forms import ImageField

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.nome


TAMANHOS = (('P', 'Pequeno'), ('M', 'Medio'), ('G', 'Grande'))
class Produto(models.Model):
    descricao = models.ForeignKey(Categoria, related_name='produtos', null=True, on_delete=models.CASCADE )
    tamanho = models.CharField(choices=TAMANHOS, max_length=1)
    
    categoria = models.ForeignKey(Categoria, related_name='produtos', null=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=150, db_index=True)
    slug = models.CharField(max_length=150, db_index=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    estoque = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    imagem = ImageField(upload_to = 'imagens-produtos', blank = True)

    def __str__(self) -> str:
        return self.nome

    def save(self, *args, **kwargs):
        print('o metado save() foi chamando')
        print(f'args{args}, kwargs {kwargs}')
        super(Produto, self).save(*args, **kwargs)
        
    
class Loja(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    email = models.EmailField()
    produtos = models.ManyToManyField(Produto, blank=True)


class Endereco(models.Model):
    logradouro = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)

    # outros atributos
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, primary_key=True)
    
    
class Funcionario(models.Model):
    gerente = models.ForeignKey('self')


class Conta(models.Model):
    descricao = models.CharField(max_length=100)
    saldo = models.FloatField()
    superior = models.ForeignKey('self')

    
    


