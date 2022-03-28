# Escreva um programa que leia dois numeros inteiros e mostre na tela:
# 
# O primeiro valor é maior
# O segundo valor é maior
# Néo existe maior, os dois são iguais

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))

if num1 > num2:
    print('O 1º número é maior que o 2º número.')
elif num2 > num1:
    print('O 2º número é maior que o 1º número.')
else:
    print('Os dois números são iguais.')