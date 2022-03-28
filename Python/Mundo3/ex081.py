# Crie um programa que vai ler vários números e coloque-os numa lista
# Depois disso, mostre:
#   a) Quantos números foram digitados.
#   b) A lista ordenada de forma decrescente.
#   c) Se o valor 5 foi digitado ou está na lista
#   d) Informar em qual posição está o número 5

numeros = list()

while True:
    numeros.append(int(input('Digite um número: ')))
    pergunta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if pergunta == 'N':
        break
print('-='*30)
print(f'Você digitou {len(numeros)} valores.')
numeros.sort(reverse=True)
print(f'A lista em ordem decrescente é {numeros}')
if 5 in numeros:
    print(f'O numero 5 está na lista na posição {numeros.index(5)}')
else:
    print('O valor 5 não foi encontrado na lista.')
