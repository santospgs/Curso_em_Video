# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triangulo
# 
# Condição de existência de um triangulo:
# Para um triangulo A-B-C, a soma de dois lados tem de ser sempre maior que o terceiro.
# Ex: A+B > C / B+C > A / A+C > B.
from time import sleep

print('-'*25)
print('ANALISADOR DE TRIÂNGULOS')
print('-'*25)

a = float(input('Medida do lado A: '))
b = float(input('Medida do lado B: '))
c = float(input('Medida do lado C: '))

print('-='*20)
print('PROCESSANDO...')
sleep(2)

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('\033[7;30;42mHabemus triângulus!\033[m')
else:
    print('\033[7;30;41mQue pena! Não forma um triângulo.\033[m')

print('-='*20)