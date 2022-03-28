# Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteia() e somaPar()
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
# mostrar a soma entre todos os valores PARES sorteados pela função anterior

from random import randint
from time import sleep

def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(1, 6):
        n = randint(1, 10)
        numeros.append(n) 
        sleep(0.4)       
        print(n, end=' ', flush=True)
    print('PRONTO!')   

def somaPar():
    soma = 0
    for i, v in enumerate(numeros):
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {numeros}, temos {soma}')

numeros = list()

sorteia()
somaPar()