# Faça um programa que etenha uma função chamada area(), que receba as dimensões
# de um terreno retangular (largura e comprimento) e mostra a área do terreno

def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno de lados {larg} x {comp} é {a:.2f} m²')


#Programa principa
print(' Controle de Terrenos')
print('-' * 30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)