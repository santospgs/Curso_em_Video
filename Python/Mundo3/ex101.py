#? sdasd
#? Crie um progrma que tenha uma função chamada de voto() que vai receber como parâmentro
#? o ano de nascimento de uma pessoa , retornando um valor literal indicando se uma pessoa
#? tem voto negado, opcional ou obrigatório nas eleições.



def voto(anoNasc):
	from datetime import date
	anoAtual = date.today().year
	idade = anoAtual - anoNasc
	
	if (idade < 16):  
		return f'Com {idade} anos: VOTO NEGADO.' #! RETURN COM VALOR LITERAL 
	elif (idade <= 18 or idade >= 65):
		return f'Com {idade} anos: VOTO OPCIONAL!'
	else:
		return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
