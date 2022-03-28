# Escreva um programa que pergunte a quantidade de km
# percorrido por um carro alugardo e a quantdade de dias 
# pelos quais ele foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado

dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km o carro rodou? '))

custo_aluguel = ((dias * 60) + (km * 0.15))

print(f'O carro foi alugado por {dias} dias e rodou {km} km(s).\nO preço a ser pago é R$ {custo_aluguel:.2f}.')