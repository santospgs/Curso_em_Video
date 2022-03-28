# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final coloque esse dicinário em ordem sabendo
# que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogos = {'jogador 1':randint(1,6),'jogador 2':randint(1,6),'jogador 3':randint(1,6),'jogador 4':randint(1,6)}

for k, v in jogos.items():
    print(f'O {k} tirou {v} no dado')
    #sleep(1)

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    
# MINHA RESOLUÇÃO
'''from random import randint
from time import sleep
rolagem = list()
jogo = dict()
ranking = list()
print('='*35)
for j in range(1,5):
    jogo['jogador'] = j
    jogo['valor dado'] = randint(1,6)
    print(f'O jogador {jogo["jogador"]} tirou {jogo["valor dado"]} no dado.')
    sleep(1)
    rolagem.append(jogo.copy())
    jogo.clear()
print('='*35)
print(f'{"= RANKING DOS JOGADORES = ":^35}')
for k, v in enumerate(rolagem):
    #print(k, v)
    if k == 0:
        ranking.append(rolagem[k])
        print(ranking[k[v]])
    else:
        maior = v['valor dado']
        if v['valor dado'] > maior:
            maior = v['valor dado']
            print(maior)'''