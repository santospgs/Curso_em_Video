# Desenvolva um programa que leio o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão

'''termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
decimo = termo + (11 - 1) * razao

for n in range (termo,decimo,razao):
    print(f'{n}',end=' -> ')
print('FIM!')'''

num = 1011
divisor = 1
len_num = len(str(num))
lista_num = []

while len_num > 0:
    n = num // divisor % 10
    divisor *= 10
    lista_num.append(n)
    len_num -= 1

for i in range(0,len(lista_num)):
    print(f'{lista_num[i]}',end='+')
