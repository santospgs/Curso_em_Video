# Crie um programa que leia o nome e o preço de vários produtos
# O programa deverá perguntar se o usuário vai continuar.
# No final mostre:
#   a) Qual é o total de gastos na compra.
#   b) Quantos produtos custam mais de R$ 1000.
#   c) Qual é o nome do produto mais barato.

cont_prod = total_compras = menor_valor = cont = 0
nome_maisBarato = ''

while True:
    
    produto_nome = str(input('Informe o nome do produto: ')).strip().upper()
    produto_preco = float(input(f'Informe o preço do produto {produto_nome}: ')) 

    total_compras += produto_preco

    if produto_preco >= 1000: cont_prod += 1
    
    cont += 1
    if cont == 1 or produto_preco < menor_valor:
        menor_valor = produto_preco
        nome_maisBarato = produto_nome
   
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar [S/N]: ')).strip().upper()        

    if pergunta == 'N':
        break
    
print(f'O total das compras é R$ {total_compras}')
print(f'{cont_prod} produtos custam mais que R$ 1000,00')
print(f'O nome do produto mais barato é {nome_maisBarato} que custa R$ {menor_valor}')