# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
# (com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário 
# receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade
# com quantos anos a pessoa vai se aposentar (considerando 35 anos de contribuição).

from datetime import date
pessoa = dict()
pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
pessoa['idade'] = date.today().year - int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['ano contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = 35 - (date.today().year - pessoa['ano contratação']) + pessoa['idade']
print('='*30)
for k, v in pessoa.items():
    print(f'- {k} tem o valor {v}')