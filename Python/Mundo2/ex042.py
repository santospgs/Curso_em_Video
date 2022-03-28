# Refaça o DESAFIO 35 dos triangulos, acrescentando o recurso
# que mostra que tipo de triangulo será formado:
#
# Equilátero, lados iguais
# Isosceles, dois lados iguais
# Escaleno, todos os lados diferentes

from time import sleep

print("-"*20)
print("Analisador de triangulos")
print("-"*20)

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

print("analisando...")
sleep(3)

if ((a + b) > c and (a + c) > b and (b + c) > a): 
    if (a == b and b == c):
        print ("Temos um triangulo equilátero")
    elif (a == b or b == c or a == c):
        print ("Temos um triangulo isosceles")
    else:
        print ("Temos um tringulo escaleno")
else:
    print ("Não forma um triangulo!")