# desenvolva um programa que leia seis numeros inteiros e mostre
# a soma apenas daqueles que forem pares. Se o valor digitado for 
# impar desconsidere-o
 
soma = 0
cont = 0
for n in range (1,7):
    num = int(input(f'Informe o {n}º valor: '))

    if (num % 2) == 0:
        soma += num
        cont += 1
print(f'a soma de todos os {cont} números pares é {soma}')
   