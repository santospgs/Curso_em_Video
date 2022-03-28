# Faça um programa que leia três números e mostre qual o maior e o qual o menor.

a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
c = int(input('Informe o terceiro número: '))

if a == b and b == c and a == c:
    print('-'*10)
    print('Os três números são iguais')
    print('-'*10)
else:
    #verificando o menor
    menor = a
    if b < a and b < c:
        menor = b
    if c < a and c < b:
        menor = c

    #verificando o maior
    maior = a
    if b > a and b > c:
        maior = b
    if c > a and c > b:
        maior = c 

    print(f'O menor valor é {menor}')
    print(f'O maior valor é {maior}')
