# Escreva um programa que leia um numero inteiro qualquer e peça
# para que o usuário escolha qual será a base de conversão.
#
# 1 para binário.
# 2 para octal.
# 3 para hexadecimal.

from time import sleep

num = int(input("Informe um número: "))

print("-"*20)
print('Escolha uma das opções abaixo:')
print(" > Opção 1 - Binário")
print(" > Opção 2 - Octal")
print(" > Opção 3 - Hexadecimal")

opcao = int(input("Digite a opção: "))
print("Convertendo...")
sleep(3)

if (opcao == 1):
    print("Você escolheu Binário")
    print(f"O número {num} em base binária é {bin(num)[2:]}")
elif (opcao == 2):
    print("Você escolheu Octal")
    print(f"O número {num} em base octal é {oct(num)[2:]}")
elif (opcao == 3):
    print("Voce escolheu Hexadecimal")
    print(f"O número {num} em hexadeciaml é {hex(num)[2:]}")
else:
    print("Opção Inválida")
    