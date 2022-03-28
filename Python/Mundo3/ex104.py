#
#? Crie um programa que tenha uma função leiaInt(), que vai funcionar de forma
#? semelhante à função input() do Python, só que fazendo a validação para aceitar
#? apenas um valor numérico.
#? Ex: n = leiaInt('Digite um n')
#   

'''
def leiaInt(num=''):
    num = str(input('Digite um numero: ')).strip('')

    while(num.isnumeric() == False):
        print(f'\033[31mERRO! Você deve digitar um número \033[0;0m')
        num = str(input('Digite um numero: ')).strip('')

    print(f'Você digitou o número {num}')

leiaInt()
'''

def leiaInt(msg):
    ok = False #1ª cond: começa com a verificação falsa
    valor = 0 #2ª cond: valor começa como 0

    # Cria um loop infinito
    while True:
        # Pega o valor do input e armazena em N
        n = str(input(msg))
        # Verifica se N é um numero
        if n.isnumeric():
            # se verdadeiro, converte N para inteiro
            valor = int(n)
            # OK passa a ser verdadeiro
            ok = True
        else:
            # Senão Exibe o erro e volta para o Loop while
            print(f'\033[31mERRO! Você deve digitar um número \033[m')

        # Caso o OK seja TRUE quebra o loop
        if ok:
            break

    # Retorna o valor
    return valor

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')