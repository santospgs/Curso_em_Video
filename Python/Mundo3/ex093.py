# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa
# vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade
# de gols feitos em cada partida. No final, tudo será guardado em um dicionário incluindo
# o total de gols feitos durante o campeonato.

jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantidade de partidas: '))
for i in range(partidas):
    gols.append(int(input(f'Gols partida {i+1}: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(jogador['gols'])
print('='*50)
print(jogador)
print('='*50)
for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('='*50)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'   => partida {i+1}: {v} gols')
    