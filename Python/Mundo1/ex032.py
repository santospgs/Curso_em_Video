# Faça um programa que leia um ano qualquer e mostre se é bissexto
from datetime import date

ano = int(input('Informe o ano (Coloque 0 para verificar o ano atual): '))

if ano == 0:
    ano = date.today().year
#Para um ano ser bissext0 ele precisa ser divisivel por 4, não divisivel por 100 e divisivel por 400
if (ano % 4) == 0 and (ano % 100) != 0 and (ano % 400) == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
 
