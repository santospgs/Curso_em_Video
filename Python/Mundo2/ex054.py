# crie um programa que:
# - leia a idade de 7 pessoas
# - mostre quantas pessoas são menores de idade
# - mostre quantas pessoas são maiores de idade (conseidere 21 anos)

totmaior = 0
totmenor = 0
for n in range(1,8):
    idade = int(input(f'Informe a idade da {n}ª pessoa: ')) 

    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'{totmaior} pessoas já são maiores de idade.')
print(f'{totmenor} pessoas já são maiores de idade.')
