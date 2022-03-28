# Faça um programa que leia o ano de nascimento de um jovem
#  e informe, de acordo com a sua idade:
#
# Se ele ainda vai se alistar ao serviço militar.
# se é a hora dele se alistar.
# Se já passou do tempo de alistamento.
#
# Seu preograma também deverá mostrar o tempo que falta
# ou passou do prazo.
from datetime import date

ano_nasc = int(input("Em que ano você nasceu?: "))
print("Qual seu sexo: 1 - Masculino, 2 - Feminino ")
sexo = int(input("Digite uma opção: "))
ano_corrente = date.today().year
idade = ano_corrente - ano_nasc

if (sexo == 1):    
    if (idade < 18):
        tempo = 18 - idade
        print(f"Você ainda vai se alistar em {ano_corrente + tempo}, faltam {tempo} anos")
    elif (idade == 18):
        print("Está na hora de se alistar")
    else:
        tempo = idade-18
        print(f"Já passaram {tempo} anos do prazo")
else:
    print("Sexo feminino, alistamento não obrigatório")
