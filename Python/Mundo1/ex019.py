#Um professor que sortear um dos seus alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o escolhido
import random

alunos = []

for aluno in range(0,4): alunos.append(input(f'Informe o aluno {aluno+1}: '))

print(f'O aluno sorteado foi: {random.choice(alunos)}')
