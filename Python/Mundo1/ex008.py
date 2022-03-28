#desafio8.py
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor = float(input('Informe uma medida em metros: '))
valor_cm = valor * 100
valor_mm = valor * 1000

print(f'O valor em centímetros é {valor_cm} cm e o valor em milímetros é {valor_mm} mm')

