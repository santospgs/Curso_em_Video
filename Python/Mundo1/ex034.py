# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# Para salários acima de R$ 1250,00 o aumento é de 10% e inferiores, de 15%.

salario = float(input('Informe seu salário: '))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
    
print(f'O aumento foi de R$ {aumento}')
print(f'Seu salário agora é de R$ {(salario + aumento):.2f}')
