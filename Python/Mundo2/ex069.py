# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada o programa deverá perguntar se o usuário
# que continuar. No final mostre:
#   a) quantas pessoas tem 18 anos.
#   b) quantos homens foram cadastrados
#   c) quantas mulheres tem menos de 20 anos.

#INPUTS E VARIÁVEIS
cont_m = cont_f = cont_idade = 0

while True:
    resposta = sexo = ' '   

    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()
    idade = int(input('Informe sua idade: '))

    if sexo == 'M': cont_m += 1
    if idade >= 18: cont_idade += 1
    if sexo == 'F' and idade < 20: cont_f += 1 

    while resposta not in 'SN':
        resposta = str(input('Quer continuar [S/N]: ')).strip().upper()

    if resposta == 'N':
        break

print('-'*40)
print(f'{cont_idade} pessoas tem 18 anos.')
print(f'{cont_m} pessoas são homens.')
print(f'{cont_f} mulheres tem menos de 20 anos.')
print('-'*40)
