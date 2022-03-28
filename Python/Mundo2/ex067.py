# Faça um programa que mostra a tabuada de vários números, um
# de cada vez, para cada valor digitado pelo usuário. O programa
# será interrompido quando o número solicitado for negativo.


# PRIMEIRA SOLUÇÃO

'''print('-='*25,end='-\n')
print(f'{"TABUADA":^50}')
print('-='*25,end='-')

num = int(input('\nInforme um número: '))
print('-'*25)
while num > 0:
    for i in range(1,11):
        print(f'{num} x {i} = {num * i}')
    num = int(input('\nInforme um número: '))'''

# SEGUNDA SOLUÇÃO MELHORADA

while True:
    num = int(input('Quer ver a tabuada de qual número: '))
    print('-'*30)
    if num < 0: break
    for i in range (1,11):
        print(f'{num} x {i} = {num * i}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADA!')
