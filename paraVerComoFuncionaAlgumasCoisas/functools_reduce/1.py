from functools import reduce

lista = list(range(1, 10))
lista2 = list(range(1, 5))

def l(qtd=30): 
    print('=-'*qtd+'=')
    
def sum(n1, n2): 
    return n1 + n2

print(lista)

print('reduce com DEF ')
print(reduce(sum, lista))
l()
print('lista2:', lista2)
print(reduce(sum, lista2))
l()
print('reduce com labda ')
print(reduce(lambda n1,n2: n1*n2, lista ))
l()
print('reduce com labda ')
print(reduce(lambda n1,n2: n1*n2, lista[:5] ))
