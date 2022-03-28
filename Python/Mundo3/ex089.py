# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo uma média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente.

alunos = []
while True:
    aluno_temp = [str(input('Nome do aluno: ')).strip().upper(), float(input('Nota 1: ')), float(input('Nota 2: '))]
    media = (aluno_temp[1] + aluno_temp[2]) / 2
    aluno_temp.append(media)
    alunos.append(aluno_temp[:])
    aluno_temp.clear()
    pergunta = str(input('Cadastrar outro aluno? [S/N]')).strip().upper()[0]
    if pergunta == 'N':
        break
print('-'*40)
print(f"{'BOLETIM ESCOLAR':^40}")
print('-'*40)
for i in range(len(alunos)):
    print(f'ALUNO: {alunos[i][0]:<15} | NOTA 1 = {alunos[i][1]}, NOTA 2 = {alunos[i][2]}, MÉDIA = {alunos[i][3]}')
print('-'*40)
exibir_aluno = str(input('Pesquisar aluno? [S/N]: ')).strip().upper()[0]
while exibir_aluno == 'S':
    cont = 0
    nome = str(input('Nome do aluno: ')).strip().upper()
    while cont < len(alunos):
        temp = alunos[:][cont]
        if temp[0] == nome:
            print('-'*40)
            print(f'Nome: {temp[0]} | Nota 1: {temp[1]} - Nota 2: {temp[2]} - Média {temp[3]}')
            print('-'*40)
        cont += 1
    exibir_aluno = str(input('Pesquisar outro aluno? [S/N]: ')).strip().upper()[0]
  