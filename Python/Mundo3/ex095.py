# Aprimore o desafio 093 para que ele funcione com vários jogadores
# incluíndo um sistema de visualizações de detalhes do aproveitamento de cada jogador.

jogadores = list()
jogador_temp = dict()
gols = list()
while True:
    total_gols = 0
    jogador_temp['nome'] = str(input('Nome: ')).strip().upper()
    jogador_temp['partidas'] = int(input('Nº de Partidas: '))
    for i in range(jogador_temp['partidas']):
        gol = int(input(f'Nº gols na partida {i+1}: '))        
        gols.append(gol)
        total_gols += gol
    jogador_temp['gols'] = gols[:]
    gols.clear()
    jogador_temp['total de gols'] = total_gols
    jogadores.append(jogador_temp.copy())
    jogador_temp.clear()
    pergunta = str(input('Inserir outro jogador [S/N]: ')).strip().upper()
    if pergunta == 'N':
        break
print('_'*70)
print(f'\033[4m{"COD.":^5}\033[m\033[4m{"|NOME":<20}\033[m\033[4m{"|PARTIDAS":<10}\033[m\033[4m{"|TOTAL DE GOLS":^14}\033[m\033[4m{"|MÉDIA DE GOLS":^20}\033[m')
for i in range(len(jogadores)):
    print(f'{i:^6}', end='')
    print(f'{jogadores[i]["nome"]:<20}', end='')
    print(f'{jogadores[i]["partidas"]:^10}', end='')
    print(f'{jogadores[i]["total de gols"]:^14}', end='')
    media = jogadores[i]["total de gols"] / jogadores[i]["partidas"]
    print(f'{media:^20.2f}')
print('_'*70)
while True:
    pergunta = int(input('Mostrar dados de qual jogador? (999 para encerrar): '))
    if pergunta == 999:
        print('Programa Finalizado!')
        break
    if pergunta >= len(jogadores):
        print(f'\033[0;41mJogador não existe.\033[m')
    else:
        print(f'LEVANTAMENTO DO JOGADOR: {jogadores[pergunta]["nome"]}')
        for i, v in enumerate(jogadores[pergunta]['gols']):
            print(f'    -> Partida {i+1} - {v} gols')
    



