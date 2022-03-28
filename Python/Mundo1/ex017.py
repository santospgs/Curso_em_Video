# Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

from math import hypot

ca = float(input('Informe o valor do cateto adjascente: '))
co = float(input('Informe o valor do cateto oposto: '))
print(f'O valor da hipotenusa é {hypot(ca,co):.1f}')

