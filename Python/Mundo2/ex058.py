# Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em 
# um número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpite foram
# necessários para vencer.

from random import randint
from random import shuffle
from time import sleep

sleep(1)
print('--- Bem vindo ao jogo de adivinhação! ---\n')
 
sleep(1)
print('Estou pensando em um número entre 0 e 10...\n')

sleep(1)
num_player = int(input('Em que número eu pensei? '))
num_computador = randint(0,10)

resposta = ['Hmmm...','Será mesmo?','Deixa eu testar aqui.','Acho que não hein']

while num_player != num_computador:
    sleep(1)
    #shuffle(resposta)
    print(choice(resposta))
    sleep(2)
    num_player = int(input('Não foi dessa vez, tente de novo: '))

print('Parabéns, você é bem esperto!')