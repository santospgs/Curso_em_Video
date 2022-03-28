# crie um programa que leia o peso de cinco pessoas. 
# No final mostre qual foi o maior e o menor peso lido.

'''
pesos = []

for pessoa in range(1,6): pesos.append(float(input(f'Informe o peso da {pessoa}ª pessoa: ')))

print(f'O maior peso é {max(pesos):.1f} kg')
print(f'O menor peso é {min(pesos):.1f} kg')
'''

maior = 0
menor = 0

for pessoa in range (1,6):
    peso = float(input(f'Informe o peso da {pessoa}ª pessoa: '))

    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(maior)
print(menor)
