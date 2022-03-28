# Desenvolva um programa que pergunte a distância de uma viagem em KM
# e calcule o preça da passagem, cobrando R$ 0,50 por km para viagens
# até 200 km e R$ 0,45 para viagens mais longas.

dist = float(input('Informe a distância da viagem: '))

'''if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45'''

preco = (dist * 0.5 if dist <= 200 else dist * 0.45)

print(f'O preço da viagem é R$ {preco:.2f}')