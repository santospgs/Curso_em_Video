# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#   a) Quantas pessoas foram cadastradas.
#   b) A média de idade do grupo.
#   c) Um lista com todas as mulheres.
#   d) Uma lista com todas as pessoas com idade acima da média.

pessoas = list()
mulheres = list()
idadeM = list()
temp = dict()
soma_idade = 0
while True:
    temp['nome'] = str(input('Nome: ')).strip().upper()
    temp['sexo'] = str(input('Sexo [M/F/O]: ')).strip().upper()[0]
    while temp['sexo'] not in 'MFO':
        temp['sexo'] = str(input('Erro! Sexo [M/F/O]: ')).strip().upper()[0]
    temp['idade'] = int(input('Idade: '))
    soma_idade += temp['idade']
    pessoas.append(temp.copy())
    if temp['sexo'] == 'F':
        mulheres.append(temp.copy())    
    temp.clear()
    pergunta = str(input('Quer continuar? [S/N]:')).strip().upper()
    while pergunta not in 'SN':
        pergunta = str(input('ERRO! Apenas S ou N:')).strip().upper()
    if pergunta == 'N':
        break
media = soma_idade / len(pessoas)
print(f'A) Foram cadastradas {len(pessoas)} pessoas')
print(f'B) A média de idade do grupo é {media:.2f}')
if len(mulheres) == 0:
    print('D) Não foi inserida nenhuma mulher.')
else:
    print('C) As mulheres cadastradas foram:')
    for i, v in enumerate(mulheres):
        print(f'    => {pessoas[i]["nome"]}')
for i, v in enumerate(pessoas):
    if v['idade'] >= (media):
        idadeM.append(pessoas[i])
print(f'D) As pessoas acima da média de idade são:')
for i in range(len(idadeM)):
    print(idadeM[i])
    