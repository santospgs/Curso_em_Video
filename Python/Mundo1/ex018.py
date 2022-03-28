'''
Faça um programa que leia um angulo qualquer e mostra na tela
o valor do seno, cosseno e tangente desse ângulo
'''
from math import *

anguloD = float(input('Informe o ângulo: '))
anguloR = radians(anguloD)

print(f'\nO ângulo informado foi: {(anguloD)}.\nO seno do ângulo é {sin(anguloR):.2f}.\nO cosseno do ângulo é {cos(anguloR):.2f}.\nA tangente do ângulo é {tan(anguloR):.2f}\n')
