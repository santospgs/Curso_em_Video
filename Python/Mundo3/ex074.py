# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
# Depois disso mostra a listagem de números gerados e também, indique o menor e o maior valor que estão na tupla

from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os números gerados foram: {numeros}')
print(f'O maior número gerado foi: {max(numeros)}')
print(f'O menor número gerado foi: {min(numeros)}')
