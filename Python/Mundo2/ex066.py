# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é
# a condição de parada. No final mostre quantos números foram digitados
# e qual foi a soma entre eles {desconsiderando o flag}


# ---- MINHA RESOLUÇÃO ----

'''num = int(input('Informe um número inteiro: '))
soma = num
cont = 0

while num != 999:
    num = int(input('Próximo número: '))
    cont += 1
    if n == 999: break
    soma += num
    
if soma > 1:
    print(f'Foram digitados {cont} números e a soma deles é {soma}')
else:
    print(f'Foi digitado {cont} número apenas')'''

# ---- RESOLUÇÃO DA AULA ----

soma = cont = 0

while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999: break
    soma += num
print(f'A soma dos {cont} valores foi {soma}')