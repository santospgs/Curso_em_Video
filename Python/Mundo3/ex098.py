# Faça um programa que tenha uma função chamada contador(), que receba três
# parâmetros: inicio, fim e passo e realize a contagem.
#
# Seu programa tem que realizar três contagens atráves da função criada:
#
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def contador(i, f, p):
    menor = i
    maior = f

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i > maior:
        maior = i
        menor = f
    for n in range(menor, maior + 1, p):
        print(i, end=' ', flush=True)
        sleep(1)
        if f < i:
            i -= p
        else:
            i += p
    print('FIM!')

'''contador(1, 10, 1)
contador(10, 0, 2)
contador(1, 103, 3)'''

contador(7,2,-1)
