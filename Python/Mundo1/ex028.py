#Escreva um programa que faça o computador 'pensar' em um numero inteiro de 
#0 a 5 e peça para o usuário tentar descobrir qual foi o numero escolhido pelo
#computador.
#
#O programa deverá escreve na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep

print('-'*45)
print('Estou pensando em um número entre 0 e 5...')
print('-'*45)

numero = int(input('Em que numero eu pensei? ')) #jogador tenta adivinhar
num_comp = randint(0,5)

print('PROCESSANDO...')
sleep(2)

if numero == num_comp:    
    print('PARABÉNS! Você acertou')
else:
    print('Não foi dessa vez. Tente novamente.')