# Crie um programa que leia um numero INTEIRO e mostre se ele é Par ou Impar

num = int(input('Digite um número inteiro qualquer: '))

if (num % 2) == 0: # o operador % representa o resto da divisão
    print(f'--{num} é PAR--')
else:
    print(f'--{num} é IMPAR--')
