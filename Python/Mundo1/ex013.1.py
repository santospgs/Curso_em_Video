# Criar um programa que mostre o preço final de um produto de acordo com a forma de pagamento
# Se pagamento a vista, desconto de 5%, se pagamento parcelado 5% de acrescimo 

preco = float(input('Insira o valor do produto R$ '))
pgto = int(input('Escolha a forma de pagamento:\n1- A vista\n2- parcelado\n>> '))

if pgto == 1:
    print(f'Pagamento à vista - desconto de 5%\nVocê irá pagar R$ {preco*0.95}')
elif pgto == 2:
    print(f'Pagamento parcelado - acréscimo de 5%\nVoce irá pagar R$ {preco*1.05}')