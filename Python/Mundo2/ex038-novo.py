# Escreva um programa que leia dois numeros inteiros e mostre na tela:
# 
# O primeiro valor é maior
# O segundo valor é maior
# Não existe maior, os dois são iguais

A = int(input("Informe o primeiro valor: "))
B = int(input("Informe o segundo valor: "))

print(f"valor 1 = {A}; valor 2 = {B}.")


if (A == B):
    print("Não existe maior, os dois valores são iguais")
elif (A > B):
    print("Valor 1 é maior")
else:
    print("valor 2 é maior")

    