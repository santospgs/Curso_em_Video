# faça um programa que leia um número inteiro e diga se ele é ou não primo

num = int(input('Informe um número inteiro: '))
total = 0
'''
if num == 1:
    print('1 não é primo')
elif (num / num) == 1 and (num / 1) == num:
    print(f'O número {num} é primo')
else:
    print('Não é primo')'''

for c in range(1,num + 1):
    if num % c == 0:
        print('\033[33m', end=' ') # destaca os divisores de amarelo
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c} \033[m', end=' ')

print(f'\nO número {num} foi divisivel {total} vezes')

# para que o número ser primo ele só pode ser divisivel por 1 e por ele mesmo, poranto só terá dois divisores.
if total == 0:
    print(f'\nO número {num} é primo')
else:
    print(f'\nO número {num} não é primo')