# Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela o N primeiros elementos de uma sequencia Fibonacci

n = int(input('Numero de termos: '))

'''f1 = 0
f2 = 1

while n != 0:
    print(f1)
    fn = f1 + f2
    f1 = f2
    f2 = fn
    n -= 1'''

f1 = 1
f0 = f1 - 1

while n != 0:
    print(f'{f1} → ', end='')
    f1 += f0
    f0 = f1 - f0
    n -= 1





    