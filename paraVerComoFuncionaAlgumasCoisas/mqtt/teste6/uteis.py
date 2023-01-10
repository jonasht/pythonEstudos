import sqlite3
from random import randint
from time import sleep
from colorama.ansi import Fore

# SELECIONANDO tudo DE pessoas
def get_dados():
    dados = sqlite3.connect('bancoDeDados.db')
    cursor = dados.cursor()
    cursor.execute("SELECT * FROM pessoas")
    pessoas = (cursor.fetchall()).copy()
    
    dados.commit()
    dados.close()
    convertido = []
    for pessoa in pessoas:
        convertido.append(list(pessoa))
    return convertido


def mostrarMatriz(matriz):
    print('\n')
    print(Fore.BLUE+'=-'*30+'='+Fore.RESET)
    for lista in matriz:
        for c in lista:
            print(f'{c:<10} ', end='')

        print()
    print(Fore.BLUE+'=-'*30+'='+Fore.RESET)
