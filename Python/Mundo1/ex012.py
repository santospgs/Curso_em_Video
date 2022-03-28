# Faça um algoritimo que leia um preço de um produto e mostro o seu novo preço com 5% de desconto

preco = float(input('Informe o preço do produto: R$ '))

valor_desconto = preco * 0.95

print(f'O valor do produto com desconto de 5% é R$ {valor_desconto:.2f}')