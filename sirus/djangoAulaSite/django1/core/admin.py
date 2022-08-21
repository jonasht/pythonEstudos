from django.contrib import admin

from .models import Produto, Cliente
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'estoque']

admin.site.register(Produto, ProdutoAdmin)
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'email', 'data_nascimento']
    