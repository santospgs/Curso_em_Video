# Crie um programa que leia dois valores e mostre um menos na tela
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))

print('\n[1] Somar')
print('[2] Multiplicar')
print('[3] Maior')
print('[4] Novos números')
print('[5] Encerrar o programa')
opcao = int(input('\nEscolha uma das opções acima: '))

while opcao not in (1,2,3,4,5):
    opcao = int(input('Opção inválida. Escolha a opção: '))

    if opcao == 1:
        s = valor1 + valor2
        print(s)
    elif opcao == 2:
        m = valor1 * valor2
        print(m)
    elif opcao == 3:
        maior = valor1
        if maior < valor2:
            maior = valor2
        print(f'O maior valor é {maior}')
    elif opcao == 4:
        valor1 = int(input('Informe o primeiro valor: '))
        valor2 = int(input('Informe o segundo valor: '))
print('Programa encerrado!')