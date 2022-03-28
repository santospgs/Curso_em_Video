# Desenvolva um programa que leia o nome, idade e sexo de cada pessoa.
# No final mostre:
# - Média de idade do grupo
# - Nome do homem mais velho
# - Quantas mulheres tem menos de 20 anos

nome_homem = ""
maior = 0
cont_mulheres = 0
soma_idades = 0
qtd_pessoas = int(input('Quantas pessoas são? '))

for p in range (1,qtd_pessoas+1):
    print('-'*8,end='')
    print(f' DADOS {p}ª PESSOA ',end='')
    print('-'*8)
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()

    if sexo == "M":
        if idade > maior:
            maior = idade
            nome_homem = nome

    if sexo == "F" and idade < 20:
        cont_mulheres += 1

    soma_idades += idade    
    media = soma_idades / qtd_pessoas
'''print('\n')
for p in range(1,qtd_pessoas+1):
    print('\n--- DADOS DA {}ª pessoa ---'.format(p))
    print('Nome: {}'.format(nome))
    print('Idade: {}'.format(idade))
    if sexo == 'M':
        sexo = 'Masculino'
    if sexo == 'F':
        sexo = 'Feminino'
    print('Sexo: {}'.format(sexo))'''

print('-'*20)
print(f'Nome do homem mais velho é: {nome_homem}')
print(f'A média das idade das {qtd_pessoas} pessoas é: {media}')
print(f'O total de mulheres com menos de 20 anos é: {cont_mulheres}')
print('-'*20)
        