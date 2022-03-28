#? 
#? Faça aum programa que tenha uma função chamada ficha(), que receba dois
#? parâmetros OPCIONAIS: o nome de um jogador e quantos gols ele marcou.
#? O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
#? dado não tenha sido informado corretamente. 

'''
def ficha(n='<desconhecido>',g=0):
	print(f'O jogador {n} fez {g} gol(s) no campeonato.')

nome = str(input('Nome do jogador: ')).capitalize()
gols = str(input('Número de gols: '))

if (gols.isnumeric()):
	gols = int(gols)
else:
	gols = 0

if (nome.strip() == ''):
	ficha(g=gols)
else:
	ficha(n,g)
'''

def ficha(nome='',gols=0):

	nome = str(input('Nome do jogador: ')).capitalize().strip()
	gols = str(input('Número de gols: '))

	nome = '<desconhecido>' if nome == '' else nome

	gols=int(gols) if gols.isnumeric() else 0

	return f'O jogador {nome} fez {gols} gol(s) no campeonato.'

print(ficha())
