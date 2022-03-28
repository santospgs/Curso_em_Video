# Crie um programa que simule o funcionamento de um caixa eletrônico
# No inicio, pergunte ao usuario qual será o valor a ser sacado
# (numero inteiro) e o programa vai informar quantas cédulas de cada valor
# serão entregue.
# OBS.: Considere que o caixa possui cédulas de R$ 50, R$20, R$10 e R$1.

notas = [50,20,10,1]
index = 0

print('='*30)
print('     BEM VINDO AO BANCO PS')
print('='*30)
valor = int(input('Informe um valor para saque: R$ '))
print('-'*30)
print('Você irá receber:')

while True:
    if index == len(notas):
        break
    qtd_notas = valor // notas[index]
    if qtd_notas != 0:
        valor = valor - (qtd_notas * notas[index])
        print('{} notas de R$ {}'.format(qtd_notas,notas[index]))
    index += 1
print('-'*30)

'''for i in range(len(notas)):
    if (valor / notas[index]) >= 1:
        print('Opção {} - {:.0f} notas de R$ {:.2f}'.format(i+1,valor / notas[index],notas[index]))
    index += 1

opcao = int(input('Escolha uma opção de saque: '))

print('Opção {} escolhida: Você receberá {} notas de R$ {:.2f}'.format(opcao-1,valor / notas[opcao-1],notas[opcao-1]))
break'''