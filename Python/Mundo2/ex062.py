# Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns
# termos. O programa encerra quando ele disser que quer mostrar 0 termos

termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razao da PA: '))
n = 10
cont = 1
opcao = 1

while opcao != 0:
    while cont <= n:
        print(f'{termo}',end=' -> ')
        termo += razao
        cont += 1
    print('PAUSA')         
    opcao = int(input('Quantos termos a mais: ')) 
    n += opcao
print(f'A progressão foi finalizada com {cont-1} termos')
print('FIM!')
