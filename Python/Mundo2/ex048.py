# Faça um programa que calcule a soma de todos os número impares
# que são multiplos de 3 e que se encontram no intervalo de 1 até 500
soma = 0
cont = 0
for n in range (1,501,2):
    if (n % 3) == 0:
        soma += n
        cont = cont + 1
        #print(n)
print(f'a soma de todos os {cont} valores é {soma}')