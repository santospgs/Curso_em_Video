# Faça um programa que ajude um jogador da MEGASENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para
# cada jogo, cadastrando tudo em uma lista.

from random import randint
palpites = []
jogo = []
print('-'*40)
print(f"{'PALPITEIRO MEGASENA':^40}")
print('-'*40)
qtde_jogos = int(input('Quantos jogos você quer fazer: '))
while len(palpites) < qtde_jogos:
    for i in range(6):
        n = randint(1,60)
        if n not in jogo:
            jogo.append(n)
    jogo.sort()
    palpites.append(jogo[:])
    jogo.clear()
print('-'*40)
for n in range(len(palpites)):
    print(f'Jogo nº {n+1}: {palpites[n]}')
print()
print(f'Para {qtde_jogos} jogos, você irá gastar R$ {qtde_jogos*4.5:.2f}')
print('-'*40)
