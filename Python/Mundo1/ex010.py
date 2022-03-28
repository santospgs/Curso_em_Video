# Crie um programa que peça um valor em reais e converta para dólares.

real = float(input('Infore o valor em reais:R$ '))
dolar = real / 5.11

print(f'O valor informado foi R$ {real} o que equivale a US$ {dolar:.2f}')