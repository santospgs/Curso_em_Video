# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
#
# a) quantas vezes o valor 9 aparece
# b) em que posição foi digitado o primeiro valor 3
# c) quais foram os números pares

n1 = int(input('Informe um valor: '))
n2 = int(input('Informe um valor: '))
n3 = int(input('Informe um valor: '))
n4 = int(input('Informe um valor: '))

numeros = (n1,n2,n3,n4)
print(f'O valor 9  aparece {numeros.count(9)} vezes')
print('-'*30)
if 3 in numeros:
    print(f'O primeiro número 3 aparece na posição {numeros.index(3)+1}')
else:
    print('O numero 3 não foi digitado')
print('-'*30)
print('Os números pares digitados são: ')
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        print(numeros[i],end=' ')    