#Crie um programa que leia um número Real qualquer pelo teclado
#e mostre na tela sua porção inteira
import math

num = float(input('Me fale um número qualquer: '))

print(f'O número inteiro é {math.trunc(num)}')
