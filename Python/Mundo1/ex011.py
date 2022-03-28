# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta rende 2m²

h = float(input('Informe a altura da parede em metros: '))
l = float(input('Informe a largura da parece em metros: '))

A = h * l
rend = 2

print(f'A quantidade de tinta necessária para pintar a parede é de {(A/rend):.2f} litros')