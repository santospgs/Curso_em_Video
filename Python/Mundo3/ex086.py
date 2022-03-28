# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final mostre a matriz na tela, com a informação correta.

matriz = []
for l in range (3):
    for c in range (3):
        matriz.append(int(input(f'Digite um número para [{l},{c}]: ')))        
c = 0
while c < len(matriz):
    if (c + 1) % 3 != 0:
        print(f'[ {matriz[c]:^5} ]', end='')
    else:
        print(f'[ {matriz[c]:^5} ]')
    c += 1 

#SOLUÇÃO GUANABARA
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'valor para [{l},{c}]'))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
'''