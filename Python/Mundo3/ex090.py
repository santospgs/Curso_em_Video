# Faça um programa que leia nome e média de um aluno guardando tambem a situação em um dicionário
# No final mostra o conteúdo da estrutura na tela.
aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip().capitalize()
aluno['média'] = float(input(f'Média de {aluno["nome"]}:  '))
if aluno['média'] < 5:
    aluno['situacao'] = 'Reprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Aprovado'
print('=-'*30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
