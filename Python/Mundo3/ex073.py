# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro
# na ordem de colocação. Depois mostre:
#
# a) Apenas os 5 primeiros colocados
# b) Os últimos 4 colocados da tabela
# c) Uma lista com os times em ordem alfabética
# d) Em que posição está o time da Chapecoense

times = ('Athletico-PR','Fortaleza','Bragantino','Palmeiras','Atletico-MG','Fluminense',\
    'Bahia','Atletico-GO','Santos','Flamengo','Corinthians','Ceara-SC','Internacional',\
    'Juventude','Sport Recife','Chapecoense','Cuiaba','São Paulo','America-MG','Gremio')

# ---- Item A ----
print('---TABELA CAMPEONATO BRASILEIRO---\n')
print('Cinco primeiros colocados:')
for pos,time in enumerate(times[0:5]):
    print(f'{pos+1}º lugar: {times[pos]}')
# ---- Item B ----
print('-'*40)
print(f'Quatro últimos colocados:')
for time in (times[-4::]):
    print(f'{times.index(time)+1}º lugar - {time}')
# ---- Item C ----
print('-'*40)    
print('Times em ordem alfabética:')
for time in sorted(times):
    print(f'{time}',end=', ')
# ---- Item D ----
print()
print('-'*40)    
print(f"O time da Chapecoense está em {times.index('Chapecoense')+1}º lugar")
