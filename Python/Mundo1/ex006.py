# Crie um algoritmo que pegue um número, mostre o seu dobro, seu triplo e a sua raiz quadrada.

num = float(input('Me diga um número qualquer: '))

numD = num * 2
numT = num * 3
numR = num ** (1/ 2)

print(f'O número informado foi {num}.\nO dobro deste número é {numD},\no triplo {numT}\ne a raiz quadrada é {numR:.2f}')
