# Faça um programa que jogue PAR ou IMPAR com o computador.
# O jogo só será interrompidor quando o jogador PERDER, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

num_comp = randint(0,10)
resultado = None
cont_vitorias = 0

while True:
    escolha_usuario = str(input('Escolha PAR ou IMPAR: ')).strip().upper()
    num_usuario = int(input('Informe um número de 0 a 10: '))
    soma = num_usuario + num_comp
    print('-'*30)
    print(num_usuario)
    print(num_comp)
    print(soma)
    resultado = 'PAR' if soma % 2 == 0 else 'IMPAR'
    
    if resultado != escolha_usuario: break
    print('-'*30)
    print('PARABÉNS, VOCÊ GANHOU!')
    print('-'*30)
    cont_vitorias += 1   

print('-'*30)
print(f'Que pena você perdeu! Seu total de vitórias é {cont_vitorias}')


