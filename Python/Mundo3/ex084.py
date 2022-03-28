# Faça um programa que leia o nome e o peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre;
#   a) Quantas pessoas foram cadastradas
#   b) Uma listagem com as pessoas mais pesadas
#   c) Uma listagem com as pessoas mais leves

pessoas = []
pessoa = []
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    pergunta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if pergunta == 'N':
        break
print('-'*30)
print(f'foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi {maior} e as pessoas mais pesadas são: ',end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ',end='')
print()
print(f'O menor peso foi {menor} As pessoas mais leves são: ',end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ',end='')