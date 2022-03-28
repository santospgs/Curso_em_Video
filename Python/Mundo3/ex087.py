# Aprimore o desafio anterior (086), mostrando no final:
#   a) A soma de todos os valores pares digitados
#   b) A soma dos valores da terceira coluna
#   c) O maior valor da segunda linha

matriz = []
soma_par = soma_3c = maior = n = 0
for l in range (3):
    for c in range (3):
        num = int(input(f'Digite um número para [{l},{c}]: '))
        matriz.append(num)
        if num % 2 == 0:
            soma_par += num
        if c == 2:
            soma_3c += num
        if l == 1:
            if num > maior:
                maior = num
print('-'*40)
while n < len(matriz):
    if (n + 1) % 3 != 0:
        print(f'[ {matriz[n]:^5} ]', end='')
    else:
        print(f'[ {matriz[n]:^5} ]')
    n += 1
print()
print(f'Soma dos números pares = {soma_par}')
print(f'Soma dos valores da 3ª coluna = {soma_3c}')
print(f'Maior valor da 2ª linha = {maior}')