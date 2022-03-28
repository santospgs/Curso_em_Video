# Faça um programa que leia 5 valores numéricos e guarde em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições.

valores = []

for cont in range(0,5):
    valores.append(int(input(f'Digite o valor para a posição {cont}: ')))
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)}, nas posições: ',end='')
for c,v_max in enumerate(range(len(valores))):
    if valores[v_max] == max(valores):
        print(c,end='...')
print()
print(f'O menor valor digitado foi {min(valores)}, nas posições: ',end='')
for c,v_min in enumerate(range(len(valores))):
    if valores[v_min] == min(valores):
        print(c,end='...')
