# Crie um programa que leia vários números e coloque-os em uma lista
# Depois disso, cria duas listas extras que vão conter apenas os valores pares
# e os valores impares digitados respectivamente.
#
# Ao final mostre o conteúdo das três listas geradas. 
numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um número: ')))    
    pergunta = str(input('Continuar [S/N]: ')).strip().upper()[0]
    if pergunta == 'N':
        break
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
    else:
        impares.append(numeros[i])
print('-'*40)
print(f'Lista completa: {numeros}')
print(f'Lista dos pares: {pares}')
print(f'Lista dos ímpares: {impares}')
