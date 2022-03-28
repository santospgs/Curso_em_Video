# Crie um programa que faça o computador jogar jokenpo com você

import random

print("Escolha umas das opções: ")
print("1 - pedra")
print("2 - papel")
print("3 - tesoura")
print(" ")

computador = random.randint(1,3)
jogador = int(input("Digite a opção: "))

print(computador)
print(jogador)

if (computador != jogador):
    if (computador == 1 and jogador == 2):
        print("Eu escolhi pedra")
        print("Você escolheu papel")
        print("Você ganhou, papel ganha de pedra")
    elif (computador == 1 and jogador == 3):
        print("Eu escolhi pedra")
        print("Você escolheu tesoura")
        print("Eu ganhei, pedra ganha de tesoura")
    elif (computador == 2 and jogador == 1):
        print("Eu escolhi papel")
        print("Você escolheu pedra")
        print("Eu ganhei, papel ganha de pedra")
    elif (computador == 2 and jogador == 3):
        print("Eu escolhi papel")
        print("Você escolheu tesoura")
        print("Você ganhou, tesoura ganha de papel")
    elif (computador == 3 and jogador == 1):
        print("Eu escolhi tesoura")
        print("Você escolheu pedra")
        print("Você ganhou, pedra ganha de tesoura")
    elif (computador == 3 and jogador == 2):
        print("Eu escolhi tesoura")
        print("Você escolheu papel")
        print("Eu ganhei, tesoura ganha de papel")

else:
    print("empate!")
    