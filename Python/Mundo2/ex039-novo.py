# Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade:
#
# Se ele ainda vai se alistar ao serviço militar.
# se é a hora dele se alistar.
# Se já passou do tempo de alistamento.
#
# Seu preograma também deverá mostrar o tempo que falta
# ou passou do prazo.

from datetime import date

ano_nasc = int(input('Informe seu ano de nascimento: '))
ano_atual = date.today().year

idade = ano_atual - ano_nasc

tempo = 18 - idade
if tempo < 0: tempo = tempo * (-1)

if idade < 18 :
    print(f"Ainda não chegou a hora. Faltam {tempo} anos")
elif idade == 18 :
    print("Sua hora chegou, soldado!")
else:
    print(f"Seu tempo já passou há {tempo} anos")


