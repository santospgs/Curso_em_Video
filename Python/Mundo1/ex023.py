# Faça um programa que leia um numero de 0 a 9999 e mostre
# na tela cada um dos dígitos separados
# -----
# Ex: Digite um numero: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

numero = int(input('Informe um número de 0 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'\nAnalisando o número {numero} ...')
print(f'unidade: {u}')
print(f'dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')
