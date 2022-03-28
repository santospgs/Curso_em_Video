#? 
#? Crie um programa que tenha uma função fatorial() que receba dois parâmentros:
#? o primeiro que indique o numero a calcular e o segundo chamdo show que será
#? um valor lógico(opcional) indicando se será mostrado ou não na tela o processo
#? de cálculo do fatorial.
#? Criar uma docstring para a função

def fatorial(n,show=False):
    """
    --> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    '''for c in range(n, 0, -1):
        f *= c    
        if (show == True):
            print(f'{c}',end=' ')'''

    while (n >= 1):        
        if(show == True):
            print(n, end='')
            if n > 1:
                print(' x ', end='')
            else:
                print(' = ', end='') 
        f *= n
        n -= 1
    return f

print('-'*20)
print(fatorial(5,True))
#help(fatorial)
