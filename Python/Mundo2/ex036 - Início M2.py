# Escreva um programa para aprovar o emprestimo bancário para a compra de uma
# casa. O programa vai perguntar o valor da casa, o salão do comprador e em
# anos ele vai pagar.
#
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
# salário ou então empréstimo será negado.

nome_cliente = str(input('Qual seu nome? ')).strip().capitalize()
valor_casa = float(input('Qual o valor da casa que quer financiar? '))
valor_salario = float(input('Qual o seu salário mensal? '))
prazo = int(input('Em quantos anos quer pagar? '))
prestacao = valor_casa/(prazo * 12)

print('-'*40)
print(f'Olá {nome_cliente}, seja bem vindo.')
print('-'*40)
print(f'O seu salário mensal é R$ {valor_salario:.2f}')
print(f'Você quer financiar uma casa no valor de R$ {valor_casa:.2f} em {prazo} anos.')
print(f"O valor da prestação será de R$ {prestacao:.2f}")
print('-'*40)

if (prestacao > (valor_salario*0.3)):
    print('\033[7;30;41mInfelizmente seu impréstimo não foi aprovado.\033[m')
else: 
    print(f'\033[7;30;42mParabéns Sr. {nome_cliente}, seu empréstimo foi aprovado!\033[m')