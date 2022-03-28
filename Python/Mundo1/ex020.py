# O mesmo professor do desafio 19 quer sortear a ordem de apresentação
# dos trabalhos dos alunos. Faça um programa, que leia o nome dos quatro aluns
# e mostre a ordem sorteada.

from random import shuffle

alunos = []

for aluno in range(0,4): alunos.append(input(f'Nome do aluno: {aluno+1}: '))

shuffle(alunos)
print(alunos)