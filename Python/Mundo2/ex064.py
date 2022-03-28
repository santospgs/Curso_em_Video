# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é
# a condição de parada. No final mostre quantos números foram digitados
# e qual foi a soma entre eles {desconsiderando o flag}

num = int(input("Informe um numero inteiro: "))
cont = 0
soma = num

while num != 999:
    print('\n- Número digitado -')
    num = int(input("Informe o próximo número: "))
    cont += 1
    if num == 999: break
    soma += num
        

print(f'Foram digitados {cont} números e a soma dele é igual a {soma}')
print('FIM!')
