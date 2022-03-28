# Faça um programa que tenha uma função maior(), que receba vários parametros com valores inteiros
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

'''def maior(*num):
    maior = 0
    for n in num:
        #print(n, end=' ')
        if n > maior:
            maior = n
    print(maior)'''

from time import sleep

def maior(*num):
    cont = maior = 0
    print('-=' * 40)
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n}', end=' ',flush=True)
        sleep(0.4)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'Foram informados {cont} valores')
    print(f'O maior valor informado foi {maior}')

maior(9,5,1,2,8,1)
maior(1,2,3)
maior()
maior(7)

